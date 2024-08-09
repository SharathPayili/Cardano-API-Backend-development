// importing blockfrost library
const Blockfrost = require("@blockfrost/blockfrost-js");
// using my api key
const API = new Blockfrost.BlockFrostAPI({
  projectId: "mainnetEGv6KABbcd4sv3r1vLpoD02y48UWjul2", // my Blockfrost project API key
});
// just normal testing method - not important
const res = Blockfrost.deriveAddress(
    '7ec9738746cb4708df52a455b43aa3fdee8955abaf37f68ffc79bb84fbf9e1b39d77e2deb9749faf890ff8326d350ed3fd0e4aa271b35cad063692af87102152',
     0,
     1,
     false,
);
console.log(res);

// fetching blockchain data for the below mentioned address
async function fetchBlockchainData() {
  try {
    const latestBlock = await API.blocksLatest();
    const networkInfo = await API.network();
    const currentEpoch = await API.epochsLatest();
    const apiHealth = await API.health();
    // input the required address using API.addresses method while using async function like await
    const addressInfo = await API.addresses(
      "addr1vynmz7juhd5an786uhwkdd6gptp0fawg7njx8jzv7hcglucssll2u"
    );
    const stakePools = await API.pools({ page: 1, count: 10, order: "asc" });

    console.log("Stake Pools:", stakePools);
    console.log("Address Info:", addressInfo);
    console.log("Network Info:", networkInfo);
    console.log("Current Epoch:", currentEpoch);
    console.log("Latest Block:", latestBlock);
    console.log("API Health:", apiHealth);
  } catch (error) {
    console.error("An error occurred:", error);
  }
}
// funciton call
fetchBlockchainData();
