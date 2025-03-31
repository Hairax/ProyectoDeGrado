FROM node:18-alpine
WORKDIR /app
RUN npm install -g pnpm

# Copy root workspace files first
COPY package.json pnpm-workspace.yaml ./
COPY pnpm-lock.yaml ./

# Copy the service package.json
COPY apps/orders-service/package.json ./apps/orders-service/

# Install dependencies
RUN pnpm install --frozen-lockfile

# Copy service source files
COPY apps/orders-service/ ./apps/orders-service/

# Set working directory to service folder
WORKDIR /app/apps/orders-service
RUN pnpm run build

EXPOSE 3001
CMD ["node", "dist/main"]
