for service in ["gateway", "products", "users", "reviews"]:
    docker_build(
        service,
        context="{}/".format(service),
        dockerfile="{}/Dockerfile".format(service)
    )
    k8s_yaml("{}/k8s.yaml".format(service))
k8s_resource("gateway", port_forwards=["8000:8000"])
