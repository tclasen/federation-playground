const { ApolloServer } = require('apollo-server');
const { ApolloGateway } = require("@apollo/gateway");

const gateway = new ApolloGateway({
  serviceList: [
    { name: 'users', url: 'http://users:8000/' },
    { name: 'reviews', url: 'http://reviews:8000/' },
    { name: 'products', url: 'http://products:8000/' },
  ],
});

const server = new ApolloServer({
  gateway,
  subscriptions: false,
});

server.listen({port: 8000}).then(({ url }) => {
  console.log(`🚀 Server ready at ${url}`);
});
