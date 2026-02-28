# -*- coding: utf-8 -*-
import os
import shutil
import sys
import json

def create_server_package():
    # 1. 定义源目录和目标目录
    project_root = os.getcwd()
    dist_dir = os.path.join(project_root, "server_dist")
    
    if os.path.exists(dist_dir):
        shutil.rmtree(dist_dir)
    os.makedirs(dist_dir)
    
    print(f"Creating server package at: {dist_dir}")
    
    # 2. 需要复制的目录列表
    dirs_to_copy = [
        "core",
        "ai_tools", 
        # "ai_konwledge", # 移除知识库目录，避免 uiautomation 依赖和隐私数据上传
        "history_data",
        "tools",
        "ai_files_tools",
        "ai_github_tools",
        "ai_soft_tools",
        "ai_time_tools",
        "ai_web_tools",
        "ani" # 包含动画配置数据，虽然服务端不显示动画，但可能逻辑依赖
    ]
    
    for d in dirs_to_copy:
        src = os.path.join(project_root, d)
        dst = os.path.join(dist_dir, d)
        if os.path.exists(src):
            shutil.copytree(src, dst, ignore=shutil.ignore_patterns('__pycache__', '*.pyc', '.git'))
            print(f"Copied: {d}")
        else:
            print(f"Warning: Directory not found: {d}")

    # 2.1 创建空的 ai_konwledge 结构以满足 import 依赖
    # skill_registry.py 导入了 ai_konwledge.web_konwledge 和 ai_konwledge.soft_konwledge
    # 我们需要在 server_dist 中创建这些目录和空的 __init__.py，以及空的模块文件
    
    konwledge_root = os.path.join(dist_dir, "ai_konwledge")
    os.makedirs(konwledge_root, exist_ok=True)
    with open(os.path.join(konwledge_root, "__init__.py"), "w") as f: f.write("")
    
    # web_konwledge 模块
    web_k_dir = os.path.join(konwledge_root, "web_konwledge")
    os.makedirs(web_k_dir, exist_ok=True)
    with open(os.path.join(web_k_dir, "__init__.py"), "w") as f: f.write("")
    
    # 创建 web_konwledge 下的空模块
    for mod in ["ai_web", "ai_web_read_info", "ai_web_check"]:
        with open(os.path.join(web_k_dir, f"{mod}.py"), "w", encoding="utf-8") as f:
            f.write("# Mock module for server\n")
            f.write("def get_web_history(*args, **kwargs):\n    return []\n")
            f.write("def check_web_usage(*args, **kwargs):\n    return {}\n")
            # 补全 ai_web.py 缺失的属性
            if mod == "ai_web":
                f.write("def add_favorite_url(*args, **kwargs): return None\n")
                f.write("def remove_favorite_url(*args, **kwargs): return None\n")
                f.write("def list_favorite_urls(*args, **kwargs): return []\n")
                f.write("def search_favorite_urls(*args, **kwargs): return []\n")
                f.write("def open_favorite_url(*args, **kwargs): return None\n")
                f.write("def open_favorite_urls_batch(*args, **kwargs): return None\n")
            # 补全 ai_web_read_info.py 缺失的属性
            if mod == "ai_web_read_info":
                f.write("def read_web_info(*args, **kwargs): return {}\n")
            # 补全 ai_web_check.py 缺失的属性
            if mod == "ai_web_check":
                f.write("def search_web_history_by_keyword(*args, **kwargs): return []\n")
                f.write("def search_web_history_by_title(*args, **kwargs): return []\n")
                f.write("def search_web_history_by_name(*args, **kwargs): return []\n")
                f.write("def search_web_history_by_url(*args, **kwargs): return []\n")
                f.write("def search_web_history_by_domain(*args, **kwargs): return []\n")
                f.write("def search_web_history_by_browser(*args, **kwargs): return []\n")
                f.write("def search_web_history_by_date(*args, **kwargs): return []\n")
                f.write("def search_web_history_by_time_range(*args, **kwargs): return []\n")
                f.write("def search_web_history_combined(*args, **kwargs): return []\n")

    # soft_konwledge 模块
    soft_k_dir = os.path.join(konwledge_root, "soft_konwledge")
    os.makedirs(soft_k_dir, exist_ok=True)
    with open(os.path.join(soft_k_dir, "__init__.py"), "w") as f: f.write("")
    
    # 创建 soft_konwledge 下的空模块
    for mod in ["ai_soft", "ai_soft_read_info", "ai_soft_check"]:
        with open(os.path.join(soft_k_dir, f"{mod}.py"), "w", encoding="utf-8") as f:
            f.write("# Mock module for server\n")
            f.write("def get_soft_history(*args, **kwargs):\n    return []\n")
            f.write("def check_soft_usage(*args, **kwargs):\n    return {}\n")
            # 补全 ai_soft.py 缺失的属性
            if mod == "ai_soft":
                f.write("def add_favorite_app(*args, **kwargs): return None\n")
                f.write("def remove_favorite_app(*args, **kwargs): return None\n")
                f.write("def list_favorite_apps(*args, **kwargs): return []\n")
                f.write("def search_favorite_apps(*args, **kwargs): return []\n")
                f.write("def open_favorite_app(*args, **kwargs): return None\n")
                f.write("def open_favorite_apps_batch(*args, **kwargs): return None\n")
            # 补全 ai_soft_read_info.py 缺失的属性
            if mod == "ai_soft_read_info":
                f.write("def read_soft_info(*args, **kwargs): return {}\n")
            # 补全 ai_soft_check.py 缺失的属性
            if mod == "ai_soft_check":
                f.write("def search_soft_history_by_keyword(*args, **kwargs): return []\n")
                f.write("def search_soft_history_by_title(*args, **kwargs): return []\n")
                f.write("def search_soft_history_by_name(*args, **kwargs): return []\n")
                f.write("def search_soft_history_by_app(*args, **kwargs): return []\n")
                f.write("def search_soft_history_by_process(*args, **kwargs): return []\n")
                f.write("def search_soft_history_by_exe_path(*args, **kwargs): return []\n")
                f.write("def search_soft_history_by_date(*args, **kwargs): return []\n")
                f.write("def search_soft_history_by_time_range(*args, **kwargs): return []\n")
                f.write("def search_soft_history_combined(*args, **kwargs): return []\n")

    # 2.2 确保 ai_time_tools/ai_email.py 能够正常工作
    # ai_email.py 依赖 ai_konwledge 目录来存储 email_tasks.json
    # 我们上面已经创建了 ai_konwledge 目录，所以应该没问题
    # 但需要确保 requirements.txt 中包含了 schedule 相关的库（如果有用到）
    # 目前 ai_email 用的是 threading.Timer，不需要额外库

    print("Created mock ai_konwledge structure for server.")

    # 3. 复制配置文件 (如果不涉及敏感信息，可以直接复制，否则创建模板)
    # 注意：为了避免本地配置覆盖云端配置（尤其是 host 和 token），我们这里只生成一个模板，或者强制修改 host 为 0.0.0.0
    config_src = os.path.join(project_root, "config.json")
    if os.path.exists(config_src):
        # 读取本地配置
        with open(config_src, "r", encoding="utf-8") as f:
            local_config = json.load(f)
        
        # 修改 server 配置适配云端
        if "server" not in local_config:
            local_config["server"] = {}
        
        local_config["server"]["host"] = "0.0.0.0" # 云端必须监听 0.0.0.0
        # auth_token 保持不变，确保客户端和云端使用相同的 token
        # 如果本地 config.json 中的 token 是 "your_secure_auth_token_here"，请确保在部署后修改它，或者在本地修改好再打包
        
        # 写入到 server_dist
        with open(os.path.join(dist_dir, "config.json"), "w", encoding="utf-8") as f:
            json.dump(local_config, f, indent=2, ensure_ascii=False)
            
        print("Generated: config.json (with host=0.0.0.0)")
        
    # 4. 生成 server_app.py
    # 注意：我们融合了原有的 .remote_chat/server/server_app.py (远程控制/网页聊天) 和 新的 Cloud Agent 功能
    server_app_content = """import os
import sys
import json
import logging
import asyncio
import shutil
from typing import Dict, Any, List

from fastapi import FastAPI, WebSocket, WebSocketDisconnect, UploadFile, File, Form, HTTPException, Query, Request
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

# 配置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# 将当前目录加入 sys.path
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

# 加载配置
CONFIG = {}
if os.path.exists(os.path.join(current_dir, "config.json")):
    try:
        with open(os.path.join(current_dir, "config.json"), "r", encoding="utf-8") as f:
            CONFIG = json.load(f)
        logger.info(f"Loaded config from {os.path.join(current_dir, 'config.json')}")
    except Exception as e:
        logger.error(f"Failed to load config.json: {e}")
else:
    logger.warning(f"config.json not found in {current_dir}")

SERVER_CONFIG = CONFIG.get("server", {})
AUTH_TOKEN = SERVER_CONFIG.get("auth_token", "default_token")
logger.info(f"Server Auth Token loaded: {AUTH_TOKEN[:4]}***")

# 尝试导入核心 Agent
try:
    from core.core_agent.Agent import AgentSession
    logger.info("AgentSession imported successfully.")
except ImportError as e:
    logger.error(f"Failed to import AgentSession: {e}")
    AgentSession = None

app = FastAPI()

# 允许跨域
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- 网页端 HTML 内容 (原 .remote_chat/server/server_app.py) ---
HTML_CONTENT = \"\"\"
<!DOCTYPE html>
<html>
    <head>
        <title>Remote Chat</title>
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1">
        <style>
            html, body {
                height: 100%;
                margin: 0;
                padding: 0;
                background: #0f1216;
                color: #e8e8e8;
                font-family: "Microsoft YaHei", Arial, sans-serif;
            }
            .app {
                display: flex;
                flex-direction: column;
                height: 100%;
            }
            .app-header {
                padding: 12px;
                background: #151a20;
                border-bottom: 1px solid #2a2f36;
            }
            .title {
                font-size: 16px;
                font-weight: 600;
                margin-bottom: 8px;
            }
            .messages {
                flex: 1;
                overflow-y: auto;
                padding: 12px;
                display: flex;
                flex-direction: column;
                gap: 10px;
            }
            .message {
                display: flex;
                align-items: flex-start;
                gap: 8px;
            }
            .message.user {
                justify-content: flex-end;
            }
            .bubble {
                max-width: 82%;
                padding: 10px 12px;
                border-radius: 12px;
                background: #1f242b;
                color: #e8e8e8;
                white-space: pre-wrap;
                word-break: break-word;
                font-size: 14px;
            }
            .message.user .bubble {
                background: #2d6cdf;
                color: #ffffff;
                border-bottom-right-radius: 4px;
            }
            .message.assistant .bubble {
                border-bottom-left-radius: 4px;
            }
            .input-bar {
                display: flex;
                gap: 8px;
                padding: 10px;
                background: #151a20;
                border-top: 1px solid #2a2f36;
            }
            #messageInput {
                flex: 1;
                resize: none;
                border-radius: 10px;
                background: #0f1216;
                color: #e8e8e8;
                border: 1px solid #2a2f36;
                padding: 10px;
                font-size: 14px;
            }
            #sendBtn {
                background: #2d6cdf;
                color: #ffffff;
                border: none;
                border-radius: 10px;
                padding: 10px 14px;
                font-weight: 600;
                min-width: 64px;
            }
        </style>
    </head>
    <body>
        <div class="app">
            <div class="app-header">
                <div class="title">AI Assistant Cloud</div>
            </div>
            <div id="messageList" class="messages"></div>
            <div class="input-bar">
                <textarea id="messageInput" rows="2" placeholder="输入你想问的问题..."></textarea>
                <button id="sendBtn">发送</button>
            </div>
        </div>

        <script>
            var wsProtocol = window.location.protocol === "https:" ? "wss://" : "ws://";
            var wsUrl = wsProtocol + window.location.host + "/ws/web";
            var ws = null;
            var messageList = document.getElementById("messageList");
            var messageInput = document.getElementById("messageInput");
            var sendBtn = document.getElementById("sendBtn");

            function connectWs() {
                ws = new WebSocket(wsUrl);
                ws.onopen = function() { console.log("Connected"); };
                ws.onmessage = function(event) {
                    var data = JSON.parse(event.data);
                    if (data.type === "chunk") {
                        appendAssistantChunk(data.text);
                    } else if (data.type === "end") {
                        finalizeAssistant();
                    } else if (data.type === "response_full") {
                        addAssistantMessage(data.text);
                    }
                };
                ws.onclose = function() { setTimeout(connectWs, 2000); };
            }

            var currentBubble = null;
            function appendAssistantChunk(text) {
                if (!currentBubble) {
                    var msg = document.createElement("div");
                    msg.className = "message assistant";
                    currentBubble = document.createElement("div");
                    currentBubble.className = "bubble";
                    msg.appendChild(currentBubble);
                    messageList.appendChild(msg);
                }
                currentBubble.textContent += text;
                messageList.scrollTop = messageList.scrollHeight;
            }
            
            function addAssistantMessage(text) {
                 var msg = document.createElement("div");
                 msg.className = "message assistant";
                 var bubble = document.createElement("div");
                 bubble.className = "bubble";
                 bubble.textContent = text;
                 msg.appendChild(bubble);
                 messageList.appendChild(msg);
                 messageList.scrollTop = messageList.scrollHeight;
            }

            function finalizeAssistant() {
                currentBubble = null;
            }

            function sendMessage() {
                var text = messageInput.value.trim();
                if (!text) return;
                
                var msg = document.createElement("div");
                msg.className = "message user";
                var bubble = document.createElement("div");
                bubble.className = "bubble";
                bubble.textContent = text;
                msg.appendChild(bubble);
                messageList.appendChild(msg);
                
                ws.send(JSON.stringify({type: "chat", text: text}));
                messageInput.value = "";
                messageList.scrollTop = messageList.scrollHeight;
            }

            sendBtn.addEventListener("click", sendMessage);
            connectWs();
        </script>
    </body>
</html>
\"\"\"

# 全局 Agent 实例 (云端大脑)
cloud_agent = None
if AgentSession:
    try:
        cloud_agent = AgentSession()
        logger.info("Cloud Agent initialized successfully.")
    except Exception as e:
        logger.error(f"Failed to initialize Cloud Agent: {e}")
        cloud_agent = None
else:
    logger.error("AgentSession class is not available.")

# 注入连接管理器到 Agent (如果 Agent 支持)
# 我们需要一个机制让 Agent 知道客户端是否在线
# 简单的做法是：Agent 在执行技能时，如果需要客户端配合，先询问 ConnectionManager

def check_client_status():
    return manager.is_desktop_online()

# 将此函数绑定到 cloud_agent (如果存在)
if cloud_agent:
    cloud_agent.check_client_online = check_client_status
    logger.info("Bound check_client_online to Cloud Agent.")

# 连接管理器
class ConnectionManager:
    def __init__(self):
        self.desktop_clients: Dict[str, WebSocket] = {} # 桌面端连接
        self.web_clients: List[WebSocket] = []          # 网页端连接

    async def connect_web(self, websocket: WebSocket):
        await websocket.accept()
        self.web_clients.append(websocket)

    def disconnect_web(self, websocket: WebSocket):
        if websocket in self.web_clients:
            self.web_clients.remove(websocket)

    async def connect_desktop(self, websocket: WebSocket, client_id: str):
        await websocket.accept()
        self.desktop_clients[client_id] = websocket

    def disconnect_desktop(self, client_id: str):
        if client_id in self.desktop_clients:
            del self.desktop_clients[client_id]

    def is_desktop_online(self):
        ""检查是否有桌面客户端在线""
        return len(self.desktop_clients) > 0

    async def broadcast_to_web(self, message: str):
        for client in self.web_clients:
            try:
                await client.send_text(message)
            except:
                pass

manager = ConnectionManager()

@app.get("/")
async def root():
    return HTMLResponse(HTML_CONTENT)

# --- 网页端 WebSocket (直接与云端大脑对话) ---
@app.websocket("/ws/web")
async def websocket_web_endpoint(websocket: WebSocket):
    await manager.connect_web(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            try:
                message = json.loads(data)
                msg_type = message.get("type")
                
                if msg_type == "chat":
                    text = message.get("text", "")
                    if text and cloud_agent:
                        # 检查客户端状态
                        is_online = manager.is_desktop_online()
                        logger.info(f"Web chat request. Client online: {is_online}")
                        
                        # 注入状态到 Agent (通过临时属性或修改 prompt，这里简单点，注入到 text)
                        # 更优雅的方式是修改 AgentSession 的 chat 方法支持 context
                        # 这里我们用一种 hack 方式：在 user text 前面加 system hint
                        
                        status_hint = ""
                        if not is_online:
                            status_hint = "[系统提示：桌面客户端当前【离线】。除了邮件发送/查询功能外，无法执行其他本地操作（如打开文件、截图等）。如果用户请求了本地操作，请礼貌拒绝并说明原因。]"
                        else:
                            status_hint = "[系统提示：桌面客户端当前【在线】。你可以正常调用本地技能。]"
                            
                        # 注意：这里我们修改了 text，可能会影响 Agent 的理解，最好是作为 system prompt 的一部分
                        # 但 AgentSession.chat 接口只接受 text。
                        # 我们尝试修改 AgentSession 的内部状态，或者 wrapper
                        
                        # 更好的方案：直接在 AgentSession 内部做判断 (我们在 core/core_agent/Agent.py 中处理)
                        # 但我们无法轻易修改 core 代码并打包。
                        # 所以我们在 text 中注入上下文是目前改动最小的方案。
                        
                        full_text = f"{status_hint}\\n用户说：{text}"
                        
                        stream_gen = cloud_agent.chat(full_text, stream=True)
                        for chunk in stream_gen:
                            await websocket.send_json({"type": "chunk", "text": chunk})
                        await websocket.send_json({"type": "end"})
                    elif not cloud_agent:
                        await websocket.send_json({"type": "error", "text": "Agent not initialized"})
            except json.JSONDecodeError:
                pass
    except WebSocketDisconnect:
        manager.disconnect_web(websocket)

# --- 桌面客户端 WebSocket (云端模式 + 远程控制) ---
@app.websocket("/ws/client")
async def websocket_desktop_endpoint(websocket: WebSocket, token: str = Query(None)):
    # 鉴权
    # 兼容处理：有些客户端库可能把 token 放在 header 或其他地方，或者 query 参数解析有差异
    # 这里增加日志以便排查
    if token != AUTH_TOKEN:
        logger.warning(f"Auth failed. Expected: {AUTH_TOKEN[:4]}***, Received: {token[:4] if token else 'None'}***")
        await websocket.close(code=1008)
        return

    # 临时 ID
    client_id = f"temp_{id(websocket)}"
    await manager.connect_desktop(websocket, client_id)
    
    try:
        while True:
            data = await websocket.receive_text()
            try:
                message = json.loads(data)
                msg_type = message.get("type")
                
                if msg_type == "client_connect":
                    # 注册客户端 ID
                    new_client_id = message.get("client_name", "local_client")
                    manager.disconnect_desktop(client_id) # 移除旧连接记录
                    manager.desktop_clients[new_client_id] = websocket # 注册新连接
                    client_id = new_client_id
                    logger.info(f"Desktop Client connected: {client_id}")
                
                elif msg_type == "chat":
                    # 桌面端请求云端大脑 (Cloud Mode)
                    text = message.get("text", "")
                    if text and cloud_agent:
                        logger.info(f"Processing cloud chat for {client_id}: {text}")
                        stream_gen = cloud_agent.chat(text, stream=True)
                        for chunk in stream_gen:
                            await websocket.send_json({"type": "chunk", "text": chunk})
                        await websocket.send_json({"type": "end"})
                    elif not cloud_agent:
                        await websocket.send_json({"type": "error", "text": "Cloud Agent not ready"})

            except json.JSONDecodeError:
                logger.error("Invalid JSON received")
                
    except WebSocketDisconnect:
        manager.disconnect_desktop(client_id)
    except Exception as e:
        logger.error(f"WebSocket Error: {e}")
        manager.disconnect_desktop(client_id)

# --- 文件同步接口 ---

@app.post("/sync/upload")
async def upload_file(file: UploadFile = File(...), path: str = Form(...), token: str = Form(None)):
    # 安全检查：只允许特定路径
    allowed_paths = [
        "core/core_data/core_chat_memory.json",
        "history_data/history_data.json"
    ]
    # 规范化路径分隔符
    path = path.replace("\\\\", "/")
    
    if path not in allowed_paths and not path.startswith("ai_konwledge/"):
        raise HTTPException(status_code=403, detail="File path not allowed")
    
    full_path = os.path.join(current_dir, path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    
    try:
        with open(full_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        logger.info(f"File uploaded: {path}")
        return {"status": "success", "path": path}
    except Exception as e:
        logger.error(f"Upload failed: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/sync/download")
async def download_file(path: str = Query(...), token: str = Query(None)):
    # 规范化路径
    path = path.replace("\\\\", "/")
    
    # 安全检查
    if ".." in path or path.startswith("/"):
        raise HTTPException(status_code=403, detail="Invalid path")
        
    full_path = os.path.join(current_dir, path)
    if not os.path.exists(full_path):
        raise HTTPException(status_code=404, detail="File not found")
        
    return FileResponse(full_path)

if __name__ == "__main__":
    # 读取配置端口
    port = SERVER_CONFIG.get("port", 8000)
    host = SERVER_CONFIG.get("host", "0.0.0.0")
    uvicorn.run(app, host=host, port=port)
"""
    with open(os.path.join(dist_dir, "server_app.py"), "w", encoding="utf-8") as f:
        f.write(server_app_content)
    print("Generated: server_app.py")

    # 5. 生成 requirements.txt
    requirements = """fastapi>=0.95.0
uvicorn>=0.22.0
websockets>=11.0
python-multipart>=0.0.6
requests>=2.28.0
aiofiles>=23.1.0
pydantic>=1.10.0
"""
    with open(os.path.join(dist_dir, "requirements.txt"), "w", encoding="utf-8") as f:
        f.write(requirements)
    print("Generated: requirements.txt")
    
    # 6. 生成启动脚本
    start_sh = """#!/bin/bash
pip install -r requirements.txt
python3 server_app.py
"""
    with open(os.path.join(dist_dir, "start.sh"), "w", encoding="utf-8") as f:
        f.write(start_sh)
        
    start_bat = """@echo off
pip install -r requirements.txt
python server_app.py
pause
"""
    with open(os.path.join(dist_dir, "start.bat"), "w", encoding="utf-8") as f:
        f.write(start_bat)
    print("Generated: start scripts")
    
    print(f"\\nServer package created successfully at: {dist_dir}")
    print("You can upload this directory to your cloud server.")

if __name__ == "__main__":
    create_server_package()
