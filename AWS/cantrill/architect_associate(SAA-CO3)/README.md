# ASSOCIATE

## IAM
- Access keys
    - Long term credentials
    - Access key es para conecatrse usango CLI, o APIS
    - IAM user puede tener max 2  access keys
    - Access keys can be deleted, created, inactive, active
    - Set of credentials public and private 
    - Rotating access key is crear nuevas, borrar viejas
    - Only roots, y user identities usan access keys, no roles
    - name / security credentials / create access

## AWS FUNDAMENTALS
- GLobal network
    - AWS regions: Centros grandotes, data centers , insfrestructure
        - Separadas apra fault tolerance, adhere to goverment policies
        - Region code: Ej:ap-southeast-2
        - Region name: Asia Pacific (Sydney)
    - AZ: (Availability zone) Isolated infrastructure inside a region (Ej:ap-southeast-2a, ap-southeast-2b and ap-southeast-2c) Para build resilence
    - AWS edge locations: Distribution locations, cerquita clientes para low altency and high speed distribution of content
- Resilient services:
    - GLobally :
        - Operates globally, single data base (1 product) data replicated en regiones
        - No tiene tal concepto de escoger regiones
        - IAM, Route 53
    - Regional
        - 1 set of data per region
        - Replicates data to availability zones (AZ)
    - AZ
        - Fails and I'm fucked

- VPC
    - Within 1 account, 1 region
    - 100% private by default
    - Private and isolated by default, except for Default VPC
    - TYpes:
        - Default VPC: 1 per region
            - Can be removed an recreated. One per region
            - VPC CIDR is always 172.31.0.0/16, same in every region
            - Insite that regional VPC, a smaller subnet in a AZ is created with /20
            - /16 es mayor que /20, entre mas alto ams peque
            - VIene con internet gateway(IGW), security group(SG) or NACL
            - Subnets has public IPv4 address

        - Custum VPC: Many per region
