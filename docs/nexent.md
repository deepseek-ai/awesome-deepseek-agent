[English](./nexent.md) | [简体中文](./nexent.zh-CN.md)

# Integrating Nexent

Nexent is a zero-code agent auto-generation platform — build agents using pure natural language.

#### 1. Install Nexent

- Ensure [Docker](https://docs.docker.com/get-started/) and Docker Compose are installed
- Run the following commands to deploy Nexent:

```bash
git clone https://github.com/ModelEngine-Group/nexent.git
cd nexent/docker
cp .env.example .env
bash deploy.sh
```

- Users in China can select "Region Optimization" during deployment for faster image pulling
- After deployment, open [http://localhost:3000](http://localhost:3000) in your browser

> ⚠️ On first deployment, save the `suadmin` super admin credentials shown in Docker logs (displayed only once). Log in and complete: Access Tenant Resources → Create Tenant → Create Tenant Admin, then use the tenant admin account for full access.

#### 2. Configure DeepSeek Models

After logging in, go to the **Model Management** page:

- Click **"Add Custom Model"** and select **LLM** as the model type
- Fill in the key settings:

| Setting      | Value                                |
| ------------ | ------------------------------------ |
| Model Name   | `deepseek-v4-flash / deepseek-v4-pro` |
| Model URL    | `https://api.deepseek.com/v1`        |
| API Key      | `<your DeepSeek API Key>`            |

- Click **"Connectivity Check"** to verify, then save

- Then set the base model in **System Model Configuration** to your newly added DeepSeek model

#### 3. Start Using

Go to **Agent Development** to create an agent, select DeepSeek as the runtime model, describe your requirements in natural language, publish, and start chatting in **Start Chat**.

You can also follow the **Quick Setup** page: Model Management → Knowledge Base → Agent Development.
