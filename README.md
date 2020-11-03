# federation-playground
A little sandbox demo to show GraphQL federation working in docker-compose and k8s.
Concept and most of the source code stolen from: (https://github.com/bogdal/ariadne-federation-demo)

## Starting up the project:

### Docker-Compose:

```
docker-compose up --build
```

### Kubernetes:

```
tilt up --hud
```

## Accessing GraphQL Playground:

Point your browser to:
```
http://localhost:8000/graphql
```

## Components:
- Gateway: Apollo-Gateway Federation Server
- Products: Flask + Ariadne
- Users: FastAPI + Ariadne
- Reviews: Ariadne Native ASGI Server
