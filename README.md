# AMD Sentinel: Privacy-First On-Device AI Retail Companion 

**Submission for AMD Slingshot Contest** **Category:** AI in Consumer Experiences  
**Team Name:** LONE CODER  
**Team Leader:** P HARI RAM NIKIL

## The Vision
Current consumer AI assistants sacrifice user privacy by sending data to the cloud. **AMD Sentinel** flips the script. It is an on-device personal curator that runs 100% locally on **AMD Ryzen™ AI** hardware. It understands your wardrobe, your budget, and your calendar to provide hyper-personalized shopping advice without your data ever leaving your PC.

##  Key Features
- **Zero-Cloud Intelligence:** All processing is done locally on the AMD NPU.
- **Local Context Awareness:** Analyzes your `wardrobe.txt` and local data to suggest outfits and products.
- **Privacy-by-Design:** No internet connection required for the "brain" to function.
- **AMD Optimized:** Purpose-built to utilize **Ryzen™ AI** and **XDNA™ Architecture** for low-latency inference.

##  Tech Stack
- **Hardware:** AMD Ryzen™ 7000/8000 Series with Ryzen AI NPU.
- **LLM:** Llama 3 (8B) Quantized (Q4_K_M).
- **Execution Environment:** LM Studio / Ollama with **ROCm/Vulkan** acceleration.
- **Language:** Python 3.10+.

##  Installation & Setup (One-Hour Quickstart)

1. **Hardware Requirements:** - An AMD Ryzen™ AI-enabled laptop/PC.
   - Latest AMD Radeon™/Ryzen™ AI drivers installed.

2. **Setup the Brain (LM Studio):**
   - Download [LM Studio](https://lmstudio.ai/).
   - Search for and download `Llama-3-8B-Instruct-GGUF`.
   - In the "Server" tab, set **GPU Offload** to "Max" and ensure it detects your **AMD GPU/NPU**.
   - Start the Local Server on port `1234`.

3. **Clone and Run:**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/amd-sentinel.git](https://github.com/YOUR_USERNAME/amd-sentinel.git)
   cd amd-sentinel
   pip install openai
   python amd_private_eye.py
