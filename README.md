# Simple YouTube Transcript Extractor

**Half the price, zero complexity. Just clean transcript text.**

Tired of complex YouTube scrapers with 25+ configuration options? We extract transcripts with **3 simple fields** at **$2.50 per 1,000 transcripts** - 50% cheaper than complex alternatives.

## 🚀 Key Features

- **💰 Best Pricing**: $2.50/1,000 transcripts (50% cheaper than complex scrapers)
- **🎯 Dead Simple**: Just paste URLs → get clean text (no configuration hell)
- **⚡ Clean Output**: Text-only results, no metadata bloat
- **🌐 Language Support**: Auto-detect or choose from 10+ languages
- **⏱️ Format Options**: Clean text, SRT timestamps, or raw VTT
- **📝 Manual + Auto**: Prefers manual subtitles, falls back to auto-generated
- **🎯 Batch Ready**: Process multiple videos in one run
- **🔄 Smart Retries**: Automatic retry with proxy rotation

## 📋 Input Configuration

### **Simple Configuration (3 fields max!)**

**Required:**
- **YouTube URLs**: Paste one or multiple video URLs

**Optional (choose what you need):**
- **Language**: Auto-detect, English, Spanish, French, etc.
- **Format**: Clean text (default), SRT with timestamps, Raw VTT
- **Prefer Manual Subtitles**: Use human-created over auto-generated

### **Input Examples**

**Basic Usage:**
```json
{
  "startUrls": [
    { "url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ" }
  ]
}
```

**Batch Processing with Timestamps:**
```json
{
  "videoUrls": [
    "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
    "https://youtu.be/abc123",
    "https://www.youtube.com/shorts/xyz789"
  ],
  "includeTimestamps": true,
  "maxRetries": 3
}
```

**With Proxy Support:**
```json
{
  "startUrls": [
    { "url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ" }
  ],
  "proxy": "http://residential-proxy.com:8080",
  "includeTimestamps": false
}
```

## 📤 Output Format

Results are presented in a user-friendly interface with detailed metadata:

### **Successful Extraction**
```json
{
  "success": true,
  "video_id": "dQw4w9WgXcQ", 
  "video_url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
  "video_title": "Rick Astley - Never Gonna Give You Up",
  "transcript": "We're no strangers to love You know the rules and so do I...",
  "transcript_length": 1247,
  "source": "ytdlp_vtt_optimized",
  "language": "en",
  "includes_timestamps": false,
  "proxy_used": "direct"
}
```

### **With Timestamps (Premium)**
```json
{
  "success": true,
  "video_title": "Rick Astley - Never Gonna Give You Up",
  "transcript": "[00:00:15] We're no strangers to love\n[00:00:18] You know the rules and so do I\n[00:00:21] A full commitment's what I'm thinking of",
  "includes_timestamps": true,
  "transcript_length": 156
}
```

### **Failed Extraction**
```json
{
  "success": false,
  "video_url": "https://www.youtube.com/watch?v=invalid",
  "error": "Could not extract video ID from URL",
  "attempts": 3,
  "source": "ytdlp_vtt_optimized"
}
```


## 🎯 Perfect Use Cases

- **Content Creators**: Generate transcripts for accessibility and SEO
- **SEO Agencies**: Analyze competitor video content and keywords  
- **Developers**: Build transcript-powered applications and chatbots
- **Researchers**: Academic analysis of video content at scale
- **Marketers**: Extract insights from customer testimonial videos
- **Educators**: Create searchable video course materials
- **Podcasters**: Convert YouTube videos to blog posts and articles


## 🏗️ Technical Specifications

- **Runtime**: Python 3.11 with Apify SDK
- **Success Rate**: 99% extraction success  
- **Processing Speed**: ~5-10 seconds per video
- **Batch Size**: Unlimited videos per run
- **Memory**: 1GB recommended
- **Timeout**: 1 hour default
- **Proxy Support**: HTTP/HTTPS/SOCKS5
- **Output Formats**: Plain text or timestamped

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

## 🚀 Getting Started

1. **Add URLs**: Paste YouTube URLs (any format supported)
2. **Configure Options**: Enable timestamps if needed
3. **Run Actor**: Process videos individually or in batches  
4. **Get Results**: Download clean transcripts with metadata
5. **Pay Only**: For successful extractions (failed = free)

## 📞 Support & Tips

**For Best Results:**
- Use publicly accessible YouTube videos
- Consider residential proxies for high-volume usage
- Verify videos have English subtitles available
- Use batch processing for cost efficiency

**Troubleshooting:**
- Check Actor logs for detailed error information
- Retry failed videos (failures are free)
- Contact support for persistent issues

## 🔄 Updates

- Regular updates to maintain YouTube compatibility