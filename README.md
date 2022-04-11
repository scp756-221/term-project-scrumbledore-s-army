# restaurant-service

## k8s Deployment Steps:
Steps to create EKS cluster and installing `istio`
```
make -f k8s.mak start
make -f k8s.mak setnamespace
make -f k8s.mak setistio
cat tools/ghcr.io-token.txt | docker login ghcr.io -u subclassy --password-stdin
make -f k8s.mak publishimage
make -f k8s.mak deployservice
```
Use `kubectl get svc --all-namespaces` to get the IP for the services.

To deploy prometheus and grafana. In the command below replace the variable names with appropriate external IPs.
```
make -f k8s.mak provision MENU='aaa' BILL='bbb' BOOK='ccc' 
```

To view Grafana dashboard, enter the below command and visit localhost:3000
```
make -f k8s.mak grafana-port-forward
```
After using the EKS cluster ensure to stop the cluster, in order to prevent absurd charges
```
make -f k8s.mak stop
```
