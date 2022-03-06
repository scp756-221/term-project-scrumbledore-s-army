# restaurant-service

## k8s Deployment Steps:
Steps to create EKS cluster and installing `istio`
```
make -f k8s.mak start
make -f k8s.mak setnamespace
make -f k8s.mak setistio
make -f k8s.mak publishimage
make -f k8s.mak deployservice
```
