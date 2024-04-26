# CLOUD PRACTITIONER ESSENTIALS

### Module 1 -  Intro AWS
   - **Client**: Browser, desktop app
    - **Server**: Service, such EC2 (Amazon Elastic COmpute Cloud)
    - **Cloud commputing** : On-demand delivery of IT resources and applications through the internet with pay-as-you-go pricing
   - **Private Could deployment**: on premise

### Module 2 - Compute in cloud
- **EC2** : 
    - Pay for what you use, running instances
    - Virtualization, shared host machine, but have different and a lot of virtual machines
    - Hypervisor: Runs in the host machine, share physical resources, coordinates multitenancy. Keeps virtual machine separe from the others.
    - Multitenancy: Sharing underlying hardware between virtual machines, not aware of others.
    - Choose OS, Linux or Windows
    - Control software: Internal bussiness, web apps, data bases, third party software ..
    - Resisable - Vertical scaling with more memory, more CPU.
    - You control networking (private or public acccess)
    - **Steps**: 
        1. Launch an instance: Choose OS, application server, or apps. Select instance type (hardware)
        2. Connect to isntance, several ways
        3. Use
    - **Instances families**:
        - _General purpose_: Application, gaming, backend servers, databases (small and medium). ej: Code repositories
        - _Compute optimized instance_ : High performance processor. Ej: Gaming, High Performance Computing (HPC)., scientific modeling
        - _Memory optimized instance_ : Fast performace large datasets in memory
        - _Accelerated computing instances_ : Hadrware cceleratos, fastoating point calculation, grapics, data petterns
        - _Storage optimized instances_ : High sequential rean and write access o large datasets. Ej: Data warehoising, High frercnency online trasnaction processiong (OLTP)
    - **Price**:
        - _On demand_ : Seconds or hours, no prior contract, baseline
        - _Savings plans_ : Commiment for ussage, 1 to 3 years, huge discount, regardless of isntance family, region, AWS Fargat and Lambda. 72% discount
        - _Reserve the instances_ : 1 to 3 years. 3 payments: upfront, partial, no upfront. 75% discount
        - _Spot instances_ : AWS can reclaimed the isntance. 2 minutes warning priot. Up to 90% disccount. Interruptions. Ej: Batch worlkloads
        - _Dedicated host_: Host for me only
- **Beneficts**
- **Scalability** : automatically respond to changing demand. 
    - Amazon EC2 auto Scaling:
        - Dynamic scaling: Responds to changing demand
        - Predictive scaling:  Schedules the right number of Amazon EC2 instances based on predicted demand
    - Configurations for auto Scaling:
        - minimum capacity: Number of Amazon EC2 instances that launch immediately after you have created the Auto Scaling group
        - Desired capacity: Default is same  as minimum
        - Maximum capacity: Maximum of four Amazon EC2 instances.
    - **Elastic Load Balancing** : automatically distributes incoming application traffic across multiple resources, such as Amazon EC2 instances. Define to which EC2 instance the request should go. 
        - Regional construct
- **Messaging and queing**
    - Tightly coupled architecture: Monolithic app. If one component fails, so the others
    - Loosely coupled: If a single component fails, the other components continue to work because they are communicating with each other
        - Aplication integration:
            - Simple Notification Service (Amazon SNS)
                - sing Amazon SNS topics, a publisher publishes messages to subscribers
            - Amazon Simple Queue Service (Amazon SQS)
### Module 3 - Global infraestructure adn reliability