import { Controller, Get } from '@nestjs/common';

@Controller()
export class AppController {
  @Get()
  healthCheck() {
    return { message: 'API Gateway funcionando 🚀' };
  }
}
