FROM node:18-alpine

WORKDIR /app

# Copiar archivos necesarios para la instalación de dependencias
COPY package.json ./
COPY pnpm-*.yaml ./
COPY apps/frontend/package.json ./apps/frontend/

# Instalar dependencias
RUN corepack enable && pnpm install --filter frontend --frozen-lockfile

# Copiar el código fuente
COPY apps/frontend/ ./apps/frontend/

# Cambiar al directorio del frontend y construir
WORKDIR /app/apps/frontend
RUN pnpm run build

EXPOSE 5173
CMD ["pnpm", "dev"]
