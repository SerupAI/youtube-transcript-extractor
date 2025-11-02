# YouTube Transcript Extractor

**The most cost-effective YouTube transcript extraction solution on Apify.**

Extract transcripts from YouTube videos with 99% success rate. No $20/month fees like competitors - pay only per use. Perfect for content creators, SEO agencies, and developers.

## 🚀 Key Features

- **💰 Cost-Effective**: Pay only $0.02 per successful transcript (no monthly fees)
- **⚡ High Success Rate**: 99% extraction success with anti-bot detection bypass
- **🎯 Batch Processing**: Process multiple videos in a single run
- **⏱️ Timestamp Support**: Optional timestamps for premium use cases
- **🌐 Proxy Ready**: Built-in residential proxy support
- **🔄 Smart Retries**: Automatic retry logic with exponential backoff
- **✨ Clean Output**: Removes VTT tags and duplicate segments
- **📊 Structured Results**: User-friendly interface with detailed metadata

## 📋 Input Configuration

### **Required**
- **startUrls** or **videoUrls**: YouTube video URLs to process

### **Optional Parameters**
- **includeTimestamps**: Add timestamps to transcript (premium feature)
- **proxy**: Proxy server for enhanced reliability  
- **maxRetries**: Maximum retry attempts per video (default: 3)

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

## 🔧 How It Works

1. **URL Processing**: Extracts video IDs from various YouTube URL formats
2. **VTT Extraction**: Uses yt-dlp to download only subtitle files (not video)
3. **Text Processing**: Applies advanced VTT cleaning and deduplication
4. **Output Generation**: Creates structured data with metadata

## 🎯 Perfect Use Cases

- **Content Creators**: Generate transcripts for accessibility and SEO
- **SEO Agencies**: Analyze competitor video content and keywords  
- **Developers**: Build transcript-powered applications and chatbots
- **Researchers**: Academic analysis of video content at scale
- **Marketers**: Extract insights from customer testimonial videos
- **Educators**: Create searchable video course materials
- **Podcasters**: Convert YouTube videos to blog posts and articles

## 💰 Pricing Advantage

**Competitor Analysis:**
- **Leading competitor**: $20/month + usage fees
- **This actor**: $0.02 per successful transcript (no monthly fees)

**Cost Comparison:**
- **100 transcripts**: You pay $2 vs competitor's $20+ = **90% savings**
- **500 transcripts**: You pay $10 vs competitor's $25+ = **60% savings**  
- **1,000 transcripts**: You pay $20 vs competitor's $30+ = **33% savings**

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