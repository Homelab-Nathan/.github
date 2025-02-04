```memaid
graph TD
  Traefik[Traefik Reverse Proxy] -->|Redirection HTTP| Caddy[Caddy Web Server]
  Caddy -->|Serve Frontend| Frontend[Frontend (React, Vue.js, etc.)]
  
  Traefik -->|Redirection API| SpringBoot[Spring Boot Backend]
  SpringBoot -->|Se Connecte à| MongoDB[MongoDB Database]
  
  subgraph Frontend [Frontend Service]
    Frontend
  end
  
  subgraph Backend [Backend Service]
    SpringBoot
    MongoDB
  end
```
