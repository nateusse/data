# Introduction to DevOps and Site Reliability Engineering by Linux Foundation

## Chapter 1: Welcome

## Chapter 2: Introduction to DevOps /SRE
- **DevOps** : Set of practices, principles, and cultural philosophies that aim to enhance collaboration and communication between software development (Dev) and IT operations (Ops) teams
- **SDLC**: Plan, build, code, test, release, deploy, operate, monitor

-**Tools**:
    - Version control: Git, github, subversion
    - Containers y orquestracion: Docker, Kubernetes, Podman
    - CI / CD: Jenkins, Travis, CircleCI 
    - Insfraestructure as a code (IaC): Terraform, AWS Cloud formation, Open Tofu
    - Management: Ansible, Chef, Puppet
    - Continius monitoring tool: Prometheus, Zabbix, Nagios, OpenNMS, Grafana
    - Loggin tools: ELK stack, fluentd, splunk
    - Source code managment tools: Bitbucket, gitlab, github

## Chapter 3: Intro to Cloud
- **Que es cloud**: Data centers accesible via internet

- **GCP create compute engine**
    1. Entrar GCP console
    2. Create project
    3. Compute Engine o create VM
    4. Configurate VM (name, region or zone, machine type for amount CPU, boot disk), firewall(network HTTP), networking (externals IP adresses, ..)security(SSH key) 

- **Advantages**
    - Escalar based in demand
    - Insfrastucture as a Code (IaC). Recursos inmediatios para new features
    - Servicios compatibles, no empezzar desde cero

- **Historia**
    - Virtualizacion 200
    - AWS 2006
    - Google 2008 App engine, 2012 GCP
    - Micorsoft Project Red dog 2008, Azure 2010
- **Cloud computing services models**
    - Plataform as a Service(PaaS):
        - Cloud provider maneja seguridad, OS network, servers, operating systems, and storage
        - Developers se concentrar en programar, no en controlar nada
        - Test, host apps mismo enviroment. I control depy app y featues del host environment
        - Ej: Me concentro en hacer mi casa
    - Infraestructure as a Services(IaaS):
        - Me dan los recursos (networks, servers, storage ), pay as you go (scale as you need)
        - No controlo undelying infraestructure.
        - EJ: Mi sitio de cnstruccion, me dan recursos (gas, agua,..) pero debo adminsitrarlos y construir casa
    - Software as a service (SaaS)
        - Todo (insfrestructure, end product) lo maneja cloud provider. Ej Dorpbox, email, ni la app, solo uso
    - FUnction as a Service
        - No manejo nada, pero no me comprometo a firmar contratos
- **Cloud deployment models**
    - Public: CLoud providers offer serources to public
        - AWS, Alibaba, IBM, GCP, Azure
    - Hibrid: On premise y cloud
        - Azure Hybrid Cloud, VMware Cloud Foundation, and CloudHesive 
    - Multi-cloud: Combinacion varias nubes
        - AWS for machine learning, Azure for integration services, and Google Cloud for data analytics
    - Private: Mi compania en un servidor completo
        - OpenStack, Hyper-V, XenServer, KVM, or VMware's vSpher
    - Comunity: Un servidor, muchas companias interes comun.
- **Cloud Services**
    - Compute services:
        - Virtual machines: computing environments
        - Containers
            - Lightweight and scalable way to package and deploy applications
            - Google Kubernetes Engine (GKE), Azure Kubernetes Service (AKS) or Rancher

    - Storage:
        - Memory:
            - Object sotrage: Amazon S3, Azure Blob Storage or wasabi,
            - Block storage: Google Cloud Persistent Disks. Mas tradicional
            - File storage: AWS Elastic File System (EFS) or Azure File Storage 
    - Database:
        - Manage, storage data
            - Relational databases: Services like AWS RDS, Azure SQL Database or DigitalOcean Managed Databases
            - Unstructured or semi-structured data, NoSQL databases like MongoDB Atlas or Google Cloud Firestore 

    - Netowrking
        - Permiten conneciones entre diferentes componentes
            - Virtual networks: such as AWS VPC, Azure Virtual Network, Oracle Cloud Infrastructure (OCI)'s Virtual Cloud Network (VCN), or DigitalOcean's Virtual Private Cloud (VPC) act as the digital infrastructure for your applications. 
            - Content Delivery Networks (CDN) like Cloudflare or Akamai speed up content delivery by caching it closer to users.

    - Security
        - Entity and Access Management (IAM) services such as AWS IAM or Azure Active Directory manage who has access to what. 
        - Encryption services like AWS KMS or Azure Key Vault add an extra layer of security by safeguarding sensitive information
    
    - Machine elarning and AI
        - Platforms like Google AI Platform or Azure Machine Learning provide tools and frameworks
        - Natural Language Processing (NLP) services such as AWS Comprehend or Google Cloud Natural Language API make it easy to analyze and understand human language.
    
    - IoT
        - AWS IoT or Azure IoT Hub help you connect, monitor, and manage IoT devices seamlessly.
        - edge computing, where processing happens closer to the data source, services like Google Cloud IoT Edge or Azure IoT Edge provide a distributed solution.

    - Serverless
        - Serverless computing is akin to outsourcing the mundane tasks, allowing developers to focus purely on writing code. 
            - Function as a Service (FaaS) offerings like AWS Lambda or Azure Functions enable you to run code in response to events without worrying about managing servers
    
    - Analytical and big data services
        - Platforms like AWS EMR or Azure HDInsight make it easy to process and analyze large datasets.
        - For data warehousing, where you need to store and query massive amounts of data quickly, services like Google BigQuery or Snowflake provide scalable solutions.


## Chapter 4: Intro to Container and Kubernetes

- **Intro**

- *Virtual machines*: 
    - FUlly isolated virtual environment.Entire hardware
    - Hypervisor: Layer para tener muchas VM
- Caracteristicas VM:
    - Strong isolated: EAch one with own OS, dependentines. Muy seguras
    - Parallel: Muchos OS en el mismo hardware, puedo correr codigo legacy
    - COmplete abastraction: I can control VM fully, me own dedicated hardware
    - Pesadas, lento inicio
    - Ideales para codigo legacy y apra apps que encesitan alta isolation
- *Container*
    - Es stanar unit, box of software que contiene o encapsula lo que mi app encesita apra correr (build como libraries, ship, run como runime einviroment) 
    - SImplifica desarrollo, escalabilidad y deploy de una app
    - Hold everything for the app to run (code, libraries, runtime environment, and system configuration)
    - Share host OS, lightweight
    - Rapido escalabilidad horizontal, facil inio y stop
    - Isonalted one from other, but a vulnerability in the OS, may affect them
    - Ideales para muchos updates y (CI/CD) workflows. Faciles de usar, lightweights
    - IDeales para deployments, testing, microservicios.

- COntainers history
    - 1970s Chroot
    - 2008 LXC Linuz container
    - 2013 Docker
    - 2014 COntainer orquestration Kubernetes
    - 2020 New alternatives, como Podman

- Container technologies
    - podman
    - Containerd
    - BuildKit
    - Kata containers
    - CRI-O   
    - KuberVirt
    - Firecracker
    - Open Containe Initiative (OCI)
    - Kpack
    - Gvisor
    - 

**Docker**
- Comands:
    - install: curl -fsSL https://get.docker.com/ | sh
    - status: sudo systemctl status docker
    - add user: sudo usermod -aG docker $USER
    - verify: docker ps
    - hello world: sudo docker container run hello-world
    - list containers: sudo docker container ls
    - help : sudo docker container ls –help
    - interact container: sudo docker container run -it ubuntu /bin/bash
    - Uninstal : student@ubuntu:~$ sudo apt-get purge docker-ce docker-ce-cli containerd.io
docker-buildx-plugin docker-compose-plugin docker-ce-rootless-extras

- PARTES DOCKER
    - *Docker engine*: Muchos modulos que ayudan el ciclo de vida
        - Containerd:
        - runC:
        - libcontainer: 
        - *Docker client* : CLI para inetractuar con DOcker daemon (engine)
        - *Docker images*: Lightweight, standalone, and executable packages that include the application and all its dependencies. Vienen de isntrucciones en el dockerfile
        - *Docker registry*: Docker images are stored in registries, which are repositories for sharing and distributing container images. Docker Hub is the default public registry; users can also set up private registries for internal use. Images can be pulled from registries when needed for running containers.
        - *Docker compose*:
            - docker-compose.yml
            - Users can describe the services, networks, and volumes in a docker-compose.yml file, making it easy to define complex applications with multiple components.
        - *Docker swarm*: users can create and manage a swarm of Docker nodes, turning them into a single virtual Docker host. Swarm enables the deployment and scaling of services across multiple containers.
        - *Networking and Storage Drivers*: COmunicaicon entre contenedores 

**Podman (Pod Manager)**
- Open source manajador de containers
- Daemonless Architecture (docker requires central daemon (dockerd) to create, run, and manage containers)
- Root and Rootless Modes 
    - Root Mode: Podman can run as root, similar to traditional Docker. This mode provides full access to all features and functionality of the system.
    - Rootless Mode: One of the significant features of Podman is its ability to run containers without root privileges. This enhances security as it reduces the risk of privilege escalation attacks.
- Use of Fork/Exec Model
    - A container forks itself and then execs the runtime (like runc or crun). 
    - Each container is its process or set of processes on the host, managed directly by the kernel and not by a long-running daemon process.
- Compatibility with Docker
    - Compatible Command line (CLI) syntax. making it easy for users to transition from Docker to Podman. 
- Pod managment
    - Alnieado con Kubernetes, Podman can also manage pods, which are groups of one or more containers sharing the same network, IPC, and PID namespaces
- Image managment
    - same image format as Docker, meaning it can pull and use images from any container registry that Docker can
    - same image/store format as Docker.
- Networking
    - supports multiple networking modes, including host networking, bridge networking, and container networking.
    - These modes are handled per container and can be set up to mimic Docker’s networking configurations
- Security
    - Running containers in a daemonless and often rootless mode inherently reduces security risks
    - SELinux, seccomp, and other security features natively provided by the Linux kernel.

- orchestracion
    - Manejar muchos containers.
    - Controlar deploy, scale, health monitoring, netowrking
    - Mejorar recursos: coran solo cuando need it
    - Deploy multi-cloud providers

**Kubernetes K8**
- Open source paltaform for automating deploy , scaling and magamen conteneirized apps.
- Utilidades:
    - Deployment across a cluster of nodes.
    - Scaling:automatically scales applications up or down based on demand. Buenos recursos
    - Load Balancing: Kubernetes evenly distributes traffic across different instances of your application, ensuring high availability and responsiveness.
    - Service Discovery: It enables applications to discover and communicate with each other, regardless of their location within the cluster.
    - Health Monitoring: Kubernetes monitors the health of your applications and automatically restarts them if they fail.
    - Security: Kubernetes provides a robust security framework for managing access control and protecting your applications.
    - Self-healing: Kubernetes restarts containers that fail, replaces containers, kills containers that don't respond to your user-defined health check, and doesn't advertise them to clients until they are ready to serve.
    - Horizontal scaling: Scale your application up and down with a simple command, with a UI, or automatically based on CPU usage.

- COmponents:
    - Control Plane Node
    - Worker Node (Minion)
    - POd
    - Replica set
    - Depployment
    - Service
    - VOlume
    - ConfigMap and Secret
    - Namesapce
    - Kubernetes Dashboard

## Chapter 5. Infrastructure as a Code (IaC)
- IaC: Describe and provision infrastructure elements through machine-readable script files
- Ventajas:
    - Configurar infrestructura con programming languages
    - Verion control infrastructure code, revisado y testeado
    - Facilita escalada, updates and teardwn
    - redce error manual
- Tools : Terraform , Azure Resource Manager

- Cateogiras
    - Declarative IaC tools:
        - TErraform, Pulumi, SaltStack
        - Declarar el deasado estado de la infraestructura (que quiero)
    - Configuration
        - COnfigurar y mantener apps en la infraestructura
        - Ansible, Chef, Puppet
    - Container orchestration
        -  Automatiza managment, deploy y escaladas de apps en containers
        - Kubernetes, Nomad, CloudHedge
    - CLoud native
        - Azure resource manager (ARM)
        - AWS cloudformation (JSON, YALM)
- Features
    - Declarative configuracion (que quiero)
    - Idempotent operations (misma configuraion muchas veces, mismo resultado)
    - Version control integration
    - Dependency managment
    - Parallel execution (muchas operaciones simultaneas)
## Chapter 6. Continuous Integration/Continuous Delivery (CI/CD)
- CI: Merge code reguarlamente from devs to central repo
    - integracion (codigo, automatic testing, crear artifacts) con rapido feedback
- CD" Automatiza cambios en produccion
- Ventajas:
    - Codigo de calidad, fast deployment , velocidad, deteccion temprana de bugs, incrementa comunicacion
    - Auto testing, deploy to stagin, release to production or not puede ser manual para salir rapidoa  emrcado, rapido feedback y monitoreo

- GitOps
    - Deployment methodology (git sogle source of true)
    - Tools: Argo CD, Flux, Tekton, Jenkins X

- Relsease strategies
    - Rolling relsease (no version, inmidiate resleas updates and features Ej: necesito cambios rapido, )
    - Feature tooglesor Flags  (features in conditionals para activarlos o no, gradual, A/B testing y experimentar EJ; New feature subset users)
    - Blue - green deployment ( 2 ambientes, prudcution and other testing, se cambian, quick rollback, inmediato, no paro)
    - canary: (New version to subset users)
    - Phased (staged) rollout (Nuevo fetaure subset users, monitoreo, control)

## Chapter 7. Intro to Observability 
- Observabilidad: Entender estado interno de un sistema basado en external outputs
- Utilidad: Los sistemas son complejos, deteccion y resoluciond e errores rapida, mejora user experience diadnistico problemas eficiente, 
- Pilares:
    - Logs: Digital records del sistema con el tiempo, detallados
        - Application logs: Eventos app (user actions, sys errors, trasnacitions)
        - System logs: Operative system para diagnistico hardware, no app pero la afecta (calls, schedlue tasks, messages from kernel)
        - Audit logs: Security events
    - metrics: High-level, views del comportamiento del sistema y su performance
        -  Util apra benchmarks, trends, alerts
        - System: Insfrestructura (CPU, memory, disk I/O, network..)
        - Application metrics: Software layer (app performance, latencia, error rates, vlomunes)
        - Bussiness metrics: (active users, conversion rates, revenue metrics..)
    - Traces:
        - Camno de inicio a final, sistem behavior, user experience.
        - Spans: Single operation
        - Context: Identidad across procesos , asociacion correcta
        - Tipos:
            - Distributed tracing: Microservices or distribued sistems, interacciones entre servicios
            - Real user monitoring (RUM): user experience
            - Synthetic monitoring  Baseline measurment vs real user data

## Chapter 8. Site Reliability Engineering (SRE)
- Large-sacle reliable services.
- Medir reability:
    - SLI (service level indicators): Monitore, alertas, regular analysis
    - SLOs (service level objectives): Nivel aceptable de confianza entre el engocio y el cliente
    - SLA (service elvel agreements)
- caracteristicas:
    - Focus reliability: Servicios confiables  y disponibles SLo SLO
    - Error budgets: Cuantifica downtime y errores en un tiempo eespecifico.
    - Measurable objectives: SLI, aspectos importantes para los clientes (latencia, disponiblidad, error, cuantificable con linea de comapracion)
    - Blame-free post mortems:no culpables
    - Automation:

- SRE vs DevOps
    - Enfoque en reliability, monitore  DeVosp mas cultural durante todo el ciclo de desarrollo

- Principios
    - Riesgo aceptable
    - SLO (target levels of reliability)
    - Simplcidad
    - Automatizacion
    - Planeacion
    - Blameless culture
    -

- Building SRE 
    - Empeiza pequeno e iterante, con emtricas, monitorea.
    - Contrata profesionales
    - Usa tools para monitore Prometheus, grafana, ELK Stack, para incidentes, PagerDuty, VictoOps, OpsGenie
    - No culpa