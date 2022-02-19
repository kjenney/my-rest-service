# my-rest-service

A REST service that is hosted on Kubernetes.

## Installation

To deploy the service first we need to create the local Docker registry and create a Kaniko executor to build and push the image.

## Create Registry

    $ kubectl apply -f registry.yaml

## Create Kaniko and deploy image

    $ kubectl apply -f kaniko.yaml

## Create Deployment

    $ kubectl apply -f my-rest-service.yaml

## Connecting to the service

    $ kubens my-rest-service
    $ kubectl port-forward svc/my-rest-service 8080:80