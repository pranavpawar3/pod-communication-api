## CDL Assignment

Code execution video - [here](https://www.youtube.com/watch?v=CqSUdVKqYY8)

Install minikube from [here](https://minikube.sigs.k8s.io/docs/start/)

Install kubectl from [here](https://kubernetes.io/docs/tasks/tools/install-kubectl-linux/)

To start the services

```bash
minikube start --driver docker
kubectl apply -f pod2.yaml
kubectl apply -f pod2-service.yaml
kubectl apply -f config.yaml
kubectl apply -f pod1.yaml
```

You can check the pod logs simultaneously to witness the pod conversation
```bash
# find the running pods
kubectl get all
kubectl logs <POD1_NAME> -f

# on another terminal window
kubectl logs <POD2_NAME> -f
```