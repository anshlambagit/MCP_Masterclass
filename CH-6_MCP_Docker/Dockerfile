FROM python:3.11-slim

# Install uv and uvx
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Set working directory to /app
WORKDIR /app

# Pre-install the tools into /usr/local/bin so they are globally accessible
# This avoids 'uvx' needing to download them inside the container
RUN uv tool install duckduckgo-mcp-server
RUN uv tool install agentic_terminal

# Install FastMCP and any other requirements
RUN pip install fastmcp

# Copy the entire project into the container
COPY . .

# Ensure the uv tools path is in the system PATH
ENV PATH="/root/.local/bin:${PATH}"

# Run the gateway using the module path
CMD ["python", "-u", "app/gateway.py"]