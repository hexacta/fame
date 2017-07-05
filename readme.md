# FAME
>Football Association Match Estimator

## Getting started
You just need git and docker to run FAME (from a [shared drive](https://docs.docker.com/docker-for-windows/#shared-drives)):
```bash
$ git clone https://github.com/hexacta/fame.git
$ cd fame
$ docker-compose up
```
After that, the app should be running on http://localhost:8080  

## Developing

### Built With
- [Vue.js](https://vuejs.org)
- Node
- Docker
- Python
- [sklearn](http://scikit-learn.org/)
- [XGBoost](https://github.com/dmlc/xgboost)

### Prerequisites
The only dependencies are git and docker. You should be able to change the code while running everything on docker.

### Production
Until we change containerize the build, you'll need `yarn` to run it:
```bash
$ yarn install
$ yarn start
```
That will run everything in production mode and publish it on http://localhost:4002

## License

MIT © [Hexacta](http://www.hexacta.com)