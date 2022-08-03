Steps to build the app image; (It's already built and pushed to my docker hub account, please pull it from there)

```bash
docker build -f Dockerfile -t pod2-image .
docker tag pod2-image pranavpawar3/pod2-image
docker push pranavpawar3/pod2-image
```