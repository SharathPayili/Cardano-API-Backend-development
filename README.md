# Cardano-API-Backend-development
Initial stage work on developing Backend to extract Cardano Blockchain data

 Repsitory to view my codes that I used to test and check available Cardano APIs

 **These are the available options of cardano API providers to explore if you want to contribute to backend development**
 - **Locally deployable APIs**
   - cardano-graphql
   - python-koios
   - cardano explorer api
 - **Public providers**
   - Bitquery (requires knowledge on graphql)
   - Blockfrost (available as javascript sdk)

**What is available in this repo right now**
- Code I used to test Koios api in python
- Code for javascript Blockfrost api using node.js

**Dependencies**
- for python code, to install required api modules use:
   ```bash
    pip3 install koios_api
   ```
- for node.js code, you will have to initialize a nodejs project and then type:
    ```bash
      npm i @blockfrost/blockfrost-js
    ```
