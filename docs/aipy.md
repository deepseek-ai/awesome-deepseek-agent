[简体中文](./aipy.zh-CN.md) | [English](./aipy.md) · [← Back](../README.md)
# Connect to AiPy (AiPy Pro)
AiPy is a general-purpose AI agent platform designed for non-technical users. Without any programming knowledge, users simply describe their needs in plain language, and AiPy automatically assembles an AI expert team (architects, engineers, testers, security auditors, etc.) to collaboratively complete complex tasks. It supports scenarios including project development, data analysis, document generation, image creation, video production, and more.
- **Official Website:** <https://www.aipyaipy.com/>
- **Download:** <https://www.aipyaipy.com/download>
#### 1. Install AiPy
Download the installation package for your platform from the [AiPy official website](https://www.aipyaipy.com/download):
- Windows (`.exe`)
- macOS (`.dmg`, supports both Intel and Apple Silicon)
After installation, launch AiPy to enter the main interface.
#### 2. Configure DeepSeek Model Service
AiPy natively supports OpenAI-compatible APIs and can directly connect to DeepSeek models.
1. In the AiPy main interface, click the **Settings** icon in the bottom-left corner.
2. In the navigation panel, open **Models** and click **Add**.
3. Select the model provider type **DeepSeek Official** — the Base URL will be filled in automatically. Then manually fill in the following:
   
| Configuration Item | Value |
|--------------------|-------|
| **Name** | `DeepSeek` |
| **API Key** | Your [DeepSeek API Key](https://platform.deepseek.com/api_keys) |
| **Model** | `deepseek-v4-pro` |
4. Save the configuration, and DeepSeek will be available in AiPy. You can also click **Set as Default** to make DeepSeek the default model.
<img width="1276" height="811" alt="image" src="https://github.com/user-attachments/assets/84a3da50-b321-488a-a4d3-4a78e66a29bb" />

#### 3. Get Started
After configuration, in the AiPy main interface dialog:
1. Describe your needs in plain language, and select the DeepSeek model on the right (if you set it as default in the previous step, it will be selected automatically). For example:
   - "Write me a Tetris game"
   - "Analyze this Excel sales data and find the fastest-growing product"
   - "Rename these 100 files by date"
   - "Write a year-end summary PPT for me"
2. AiPy will automatically assemble an expert team and complete the task step by step.
<img width="1123" height="728" alt="image" src="https://github.com/user-attachments/assets/efee3837-7f41-48dc-acc6-a8e50cc0a36e" />

#### 4. Advanced Usage
After completing the DeepSeek configuration, you can fully leverage its capabilities in the following AiPy scenarios:
- **Data Analysis**: Upload Excel/CSV files, and AiPy will automatically use DeepSeek for data interpretation, trend analysis, and chart generation.
- **Document Generation**: Input requirement descriptions, and AiPy uses DeepSeek's task planning capabilities combined with tools to generate documents in Word, PDF, PPT, HTML report, and other formats.
#### 5. Model Selection Guide
| Scenario | Recommended Model | Description |
|----------|-------------------|-------------|
| Complex data analysis, multi-step tasks | `deepseek-v4-pro` | Strongest reasoning capability, supports deep thinking |
| Simple Q&A, quick responses | `deepseek-v4-flash` | Fast speed, low cost |
| Code generation & debugging | `deepseek-v4-pro` | Supports Tool Calls, can invoke external tools |
