# JENKINS

- Caracteristicas
    - Escrito en Java, needs 11 or 17
    - Free
    - LTS cada 12 weeks, regular each week
    - Tomcat , puerto 8080

- CI
    - Originating from the extreme programming methodology. 
    - Automated software build y UNIT test for every change committed to the version control system by the developers.
    - Proceso:
        - Desarrollador ahce push a repo central
        - Repo central o source control trigger a build
        - Ese build run test
        - Test reportados al desarrollador, con feedback

- CD
    - Release cambios rapidos (fixed bugs, new features..)
    - Despues del CI, deploys artefeactos (from build) to staging test , si apsa, A produccion (apbocacion manual o automatica)
    - Proprizar deployment sobre new features, que a su vez se prioriza sobre arreglar bugs
    - Fast feedback
    - Continuous Delivery pipelines
        - Automatizar, monotorear progreso, feedback rapido, codigo de calidad.
        - Tools: 
            - Git, Jenkins (CI)
            - test frameworks, xUnit o Selenium.
            -  Binary repos such Artifactory tos tore build artifcats. 
            - Mangement toosl such Ansible
            - Slack o mail apra feedback
        - Free tools:
            - GitLab (no peudo escoger VC ni repos que queiro)
            - Jenkins. 
        - Paid:
            - AWS codepipeline, Circle CI, Azure pipelines, github actions, travis CI, google cloud build ..


