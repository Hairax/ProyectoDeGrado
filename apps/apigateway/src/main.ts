import { NestFactory } from '@nestjs/core';
import { AppModule } from './app.module';
import { Logger } from '@nestjs/common';

async function bootstrap() {
  const app = await NestFactory.create(AppModule);

  app.enableCors(); // Permitir peticiones desde el frontend

  const PORT = process.env.PORT || 8081;
  await app.listen(PORT, () => {
    Logger.log(`🚀 API Gateway corriendo en http://localhost:${PORT}`);
  });
}
bootstrap();
