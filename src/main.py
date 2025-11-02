"""YouTube Transcript Extractor Actor

This Apify Actor extracts transcripts from YouTube videos using an optimized 
yt-dlp VTT subtitle approach. It's designed to bypass YouTube's bot detection by using
residential proxies and advanced transcript extraction methods.

Features:
- Optimized VTT subtitle extraction
- Smart text cleaning and duplicate removal
- Residential proxy support
- Error handling and retry logic
- Structured output format
"""

from __future__ import annotations

import asyncio
import subprocess
import tempfile
import re
import os
import hashlib
from pathlib import Path
from typing import Optional, Dict, Any

from apify import Actor


class YouTubeTranscriptExtractor:
    """YouTube transcript extractor using optimized VTT processing"""
    
    def __init__(self):
        self.timestamp_regex = re.compile(r'^\d+$|^\d{1,2}:\d{2}(:\d{2})?(\.\d{3})?$')
        self.tag_regex = re.compile(r'<[^>]*>')
    
    def extract_video_id(self, url: str) -> Optional[str]:
        """Extract video ID from YouTube URL"""
        patterns = [
            r'(?:https?://)?(?:www\.)?youtube\.com/watch\?v=([a-zA-Z0-9_-]{11})',
            r'(?:https?://)?(?:www\.)?youtu\.be/([a-zA-Z0-9_-]{11})',
            r'(?:https?://)?(?:www\.)?youtube\.com/shorts/([a-zA-Z0-9_-]{11})',
            r'(?:https?://)?(?:www\.)?youtube\.com/embed/([a-zA-Z0-9_-]{11})',
        ]
        
        for pattern in patterns:
            match = re.search(pattern, url)
            if match:
                return match.group(1)
        
        return None
    
    def is_timestamp_line(self, line: str) -> bool:
        """Check if line is a timestamp"""
        return bool(self.timestamp_regex.match(line))
    
    def remove_vtt_tags(self, text: str) -> str:
        """Remove VTT formatting tags"""
        return self.tag_regex.sub('', text)
    
    def format_vtt_timestamp(self, vtt_time: str) -> str:
        """Format VTT timestamp for display"""
        # VTT timestamps are in format "00:00:01.234" - convert to "00:00:01"
        parts = vtt_time.split(".")
        if len(parts) > 0:
            return parts[0]
        return vtt_time
    
    def process_vtt_file(self, vtt_file: Path, include_timestamps: bool = False) -> str:
        """Process VTT file using optimized approach for clean text extraction"""
        try:
            with open(vtt_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Debug: Check if file has content
            if not content.strip():
                Actor.log.debug("VTT file is empty")
                return ""
            
            # Split into lines
            lines = content.split('\n')
            text_builder = []
            seen_segments = set()
            current_timestamp = None
            
            for line in lines:
                line = line.strip()
                
                # Skip WEBVTT header and empty lines
                if (line == "" or 
                    line == "WEBVTT" or
                    line.startswith("NOTE") or 
                    line.startswith("STYLE") or
                    line.startswith("Kind:") or 
                    line.startswith("Language:")):
                    continue
                
                # Check if this line is a timestamp
                if "-->" in line:
                    if include_timestamps:
                        # Extract start time for timestamp
                        parts = line.split(" --> ")
                        if len(parts) >= 1:
                            current_timestamp = self.format_vtt_timestamp(parts[0])
                    continue
                
                # Skip numeric sequence identifiers
                if self.is_timestamp_line(line) and not ":" in line:
                    continue
                
                # Remove VTT formatting tags
                clean_line = self.remove_vtt_tags(line)
                
                if clean_line != "":
                    # Smart duplicate detection
                    if clean_line not in seen_segments:
                        if include_timestamps and current_timestamp:
                            text_builder.append(f"[{current_timestamp}] {clean_line}")
                        else:
                            text_builder.append(clean_line)
                        seen_segments.add(clean_line)
            
            # Join with appropriate separator
            if include_timestamps:
                result = "\n".join(text_builder)  # New lines for timestamped content
            else:
                result = " ".join(text_builder)   # Spaces for plain text
            
            Actor.log.debug(f"Extracted {len(result)} characters from VTT")
            return result
            
        except Exception as e:
            Actor.log.error(f"Error processing subtitle file: {e}")
            return ""
    
    async def extract_transcript(self, video_url: str, proxy: Optional[str] = None, include_timestamps: bool = False) -> Dict[str, Any]:
        """Extract transcript using optimized yt-dlp VTT approach"""
        
        video_id = self.extract_video_id(video_url)
        if not video_id:
            raise ValueError(f"Could not extract video ID from URL: {video_url}")
        
        Actor.log.info(f"Extracting transcript for video ID: {video_id}")
        
        # Create temp directory for VTT files
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_path = Path(temp_dir)
            vtt_dir = temp_path / f"youtube-{video_id}"
            vtt_dir.mkdir(parents=True, exist_ok=True)
            
            try:
                # Build optimized yt-dlp command
                youtube_url = f"https://www.youtube.com/watch?v={video_id}"
                output_template = str(vtt_dir / "%(title)s.%(ext)s")
                
                cmd = [
                    "yt-dlp",
                    "--write-auto-subs",
                    "--sub-lang", "en",
                    "--skip-download",
                    "--sub-format", "vtt", 
                    "--quiet",
                    "--no-warnings",
                    "-o", output_template,
                    youtube_url
                ]
                
                # Add proxy if provided
                if proxy:
                    cmd.extend(["--proxy", proxy])
                
                Actor.log.info(f"Extracting subtitles...")
                
                # Run yt-dlp command
                result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
                
                if result.returncode != 0:
                    error_msg = f"yt-dlp failed with return code {result.returncode}: {result.stderr}"
                    Actor.log.error(error_msg)
                    raise RuntimeError(error_msg)
                
                # Find VTT files
                vtt_files = list(vtt_dir.rglob("*.vtt"))
                
                if not vtt_files:
                    raise RuntimeError("No VTT files found")
                
                # Use first VTT file found
                vtt_file = vtt_files[0]
                Actor.log.info(f"Processing subtitle file...")
                
                # Process VTT file using optimized approach
                transcript_text = self.process_vtt_file(vtt_file, include_timestamps)
                
                if not transcript_text or len(transcript_text.strip()) == 0:
                    raise RuntimeError("No transcript content found in VTT file")
                
                Actor.log.info(f"Successfully extracted transcript: {len(transcript_text)} characters")
                
                # Get video title from VTT filename
                video_title = vtt_file.stem.replace('.en', '').replace('.vtt', '')
                
                return {
                    "success": True,
                    "video_id": video_id,
                    "video_url": video_url,
                    "video_title": video_title,
                    "transcript": transcript_text.strip(),
                    "transcript_length": len(transcript_text.strip()),
                    "source": "ytdlp_vtt_optimized",
                    "language": "en",
                    "proxy_used": proxy if proxy else "direct",
                    "includes_timestamps": include_timestamps
                }
                
            except subprocess.TimeoutExpired:
                raise RuntimeError("yt-dlp command timed out after 120 seconds")
            except Exception as e:
                Actor.log.error(f"Transcript extraction failed: {e}")
                raise


async def main() -> None:
    """Main entry point for the YouTube Transcript Extractor Actor"""
    
    async with Actor:
        # Actor.log.set_level('INFO')  # Default level is already INFO
        Actor.log.info('🎬 YouTube Transcript Extractor Actor started!')
        
        # Get input from the Actor
        actor_input = await Actor.get_input() or {}
        
        # Extract configuration
        start_urls = actor_input.get('startUrls', [])
        video_urls = actor_input.get('videoUrls', [])
        proxy = actor_input.get('proxy')
        max_retries = actor_input.get('maxRetries', 3)
        include_timestamps = actor_input.get('includeTimestamps', False)
        
        # Combine URLs from both sources
        all_urls = []
        
        # Process startUrls format (Apify standard)
        for start_url in start_urls:
            if isinstance(start_url, dict):
                url = start_url.get('url')
                if url:
                    all_urls.append(url)
            elif isinstance(start_url, str):
                all_urls.append(start_url)
        
        # Process videoUrls format (direct list)
        if video_urls:
            all_urls.extend(video_urls)
        
        if not all_urls:
            Actor.log.error('No video URLs provided in input')
            await Actor.fail('No video URLs provided. Please provide URLs in startUrls or videoUrls fields.')
            return
        
        Actor.log.info(f'Processing {len(all_urls)} video URLs')
        
        # Initialize extractor
        extractor = YouTubeTranscriptExtractor()
        
        # Process each URL
        for i, video_url in enumerate(all_urls, 1):
            Actor.log.info(f'Processing video {i}/{len(all_urls)}: {video_url}')
            
            retry_count = 0
            success = False
            last_error = None
            
            while retry_count < max_retries and not success:
                try:
                    # Extract transcript
                    result = await extractor.extract_transcript(video_url, proxy, include_timestamps)
                    
                    # Save to dataset
                    await Actor.push_data(result)
                    
                    Actor.log.info(f'✅ Successfully extracted transcript for: {video_url}')
                    success = True
                    
                except Exception as e:
                    retry_count += 1
                    last_error = str(e)
                    
                    Actor.log.warning(f'❌ Attempt {retry_count}/{max_retries} failed for {video_url}: {e}')
                    
                    if retry_count < max_retries:
                        Actor.log.info(f'⏳ Retrying in 5 seconds...')
                        await asyncio.sleep(5)
            
            if not success:
                # Save failed result
                failed_result = {
                    "success": False,
                    "video_url": video_url,
                    "error": last_error,
                    "attempts": max_retries,
                    "source": "ytdlp_vtt_optimized"
                }
                await Actor.push_data(failed_result)
                Actor.log.error(f'❌ Failed to extract transcript after {max_retries} attempts: {video_url}')
        
        Actor.log.info('🎉 YouTube Transcript Extractor Actor finished!')


if __name__ == '__main__':
    asyncio.run(main())