```memaid
architecture-beta
  group api(cloud)[API]

  service traefik(reverse-proxy)[Traefik] in api
  service caddy(frontend)[Caddy] in api
  service springboot(backend)[Spring Boot] in api
  service mongo(mongo-db)[MongoDB] in api

  traefik:L -- R:caddy
  traefik:L -- R:springboot
  springboot:L -- R:mongo
```

```mermaid
graph TD
    A[Enter Chart Definition] --> B(Preview)
    B --> C{decide}
    C --> D[Keep]
    C --> E[Edit Definition]
    E --> B
    D --> F[Save Image and Code]
    F --> B
```
