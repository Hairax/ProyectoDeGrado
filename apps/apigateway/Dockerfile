FROM node:18-alpine
WORKDIR /app
RUN npm install -g pnpm

# Copy root workspace files first
COPY package.json pnpm-workspace.yaml ./
COPY pnpm-lock.yaml ./

# Copy the service package.json
COPY apps/apigateway/package.json ./apps/apigateway/

# Install dependencies
RUN pnpm install --frozen-lockfile

# Copy service source files
COPY apps/apigateway/ ./apps/apigateway/

# Set working directory to service folder
WORKDIR /app/apps/apigateway
RUN pnpm run build

EXPOSE 8081
CMD ["node", "dist/main"]
