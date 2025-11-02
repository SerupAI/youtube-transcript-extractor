# YouTube Transcript Extractor

A powerful Apify Actor that extracts transcripts from YouTube videos using an optimized yt-dlp VTT subtitle approach. Designed to bypass YouTube's bot detection while providing clean, accurate transcripts.

## 🚀 Features

- **Optimized Extraction**: Uses proven VTT subtitle extraction techniques
- **VTT Subtitle Processing**: Extracts subtitles directly instead of downloading video files
- **Smart Text Cleaning**: Removes VTT formatting tags and duplicate segments
- **Bot Detection Bypass**: Optimized for success with YouTube's anti-bot measures
- **Proxy Support**: Works with residential proxies for enhanced reliability
- **Retry Logic**: Automatic retries with exponential backoff
- **Structured Output**: Clean JSON output with metadata

## 📋 Input

The Actor accepts the following input parameters:

### Required
- **startUrls** or **videoUrls**: YouTube video URLs to process

### Optional
- **proxy**: Proxy server for requests (recommended: residential proxy)
- **maxRetries**: Maximum retry attempts per video (default: 3)

### Input Examples

**Using startUrls (Apify standard format):**
```json
{
  "startUrls": [
    { "url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ" },
    { "url": "https://youtu.be/abc123" }
  ],
  "proxy": "http://residential-proxy.com:8080",
  "maxRetries": 3
}
```

**Using videoUrls (simple array):**
```json
{
  "videoUrls": [
    "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
    "https://youtu.be/abc123"
  ],
  "maxRetries": 2
}
```

## 📤 Output

The Actor outputs structured data to the dataset with the following format:

### Successful Extraction
```json
{
  "success": true,
  "video_id": "dQw4w9WgXcQ",
  "video_url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
  "video_title": "Rick Astley - Never Gonna Give You Up",
  "transcript": "We're no strangers to love You know the rules and so do I...",
  "transcript_length": 1247,
  "source": "fabric_ytdlp_vtt",
  "language": "en",
  "proxy_used": "http://residential-proxy.com:8080"
}
```

### Failed Extraction
```json
{
  "success": false,
  "video_url": "https://www.youtube.com/watch?v=invalid",
  "error": "Could not extract video ID from URL",
  "attempts": 3,
  "source": "fabric_ytdlp_vtt"
}
```

## 🔧 How It Works

1. **URL Processing**: Extracts video IDs from various YouTube URL formats
2. **VTT Extraction**: Uses yt-dlp to download only subtitle files (not video)
3. **Text Processing**: Applies advanced VTT cleaning and deduplication
4. **Output Generation**: Creates structured data with metadata

## 🎯 Use Cases

- **Content Analysis**: Extract transcripts for AI analysis and summarization
- **SEO Research**: Analyze video content for keyword research
- **Accessibility**: Create accessible text versions of video content
- **Data Mining**: Bulk extract transcripts for research purposes
- **Integration**: Feed transcripts to other automation workflows

## 🏗️ Technical Details

- **Runtime**: Python 3.11 with Apify SDK
- **Dependencies**: yt-dlp, apify, requests
- **Memory**: 1GB recommended
- **Timeout**: 1 hour default
- **Proxy Support**: HTTP/HTTPS/SOCKS5

## 🔒 Privacy & Ethics

- Only extracts publicly available subtitle data
- Respects YouTube's robots.txt and rate limits
- No video content is downloaded or stored
- Designed for legitimate research and accessibility use cases

## 🛠️ Integration

This Actor can be easily integrated into:

- **Apify Console**: Run directly from the Apify platform
- **API Calls**: Trigger via Apify API
- **Zapier/Make**: Connect to automation workflows
- **Custom Applications**: Use with any application via REST API

## 📞 Support

For issues or questions:
- Check the Actor logs for detailed error information
- Ensure video URLs are publicly accessible
- Consider using residential proxies for better success rates
- Verify video has English subtitles available

## 🔄 Updates

- **v1.0.0**: Initial release with optimized VTT extraction
- Regular updates to maintain YouTube compatibility