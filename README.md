# json2securexml
My first project !!! Fetch a secure xml file for provided json file i.e, json to xml conversion along with encryption and decryption functionality

## Learning Project

Basic python scripting and docker understanding is required.


## Usage of docker-compose file
The below command will build the image from docker file.
`docker-compose up --build`
   - Two containers will be created here to perform the encryption and decryption
   - use `docker-compose logs` to view the logs
   - In docker-compose file the command section is responsible for executig the script.
   - encrypt.py requires `sample.json` file and arguments `--generate --encrypt`
   - decrypt.py requires the `encrypted.xml` which is output form the encrypt.py execution and arguments `--decrypt`



### encrypt.py

Usage:

`python encrypt.py sample.json --generate --encrypt`


### Improvements planned
1. Add a json validator using jsonschema python module.
2. Provide option for only convertion.
3. 
