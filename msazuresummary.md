# MS Azure Summary

### Resource Groups
It is used to group resources as a project/ptogram or architecture, environment. Here you can create your cloud resources.
The reources are VMs, DBs, virtual networks...
Within the Resource Groups there are some features and configurations to be exploired such as Activity Log, IAM (permissions), Tags, Settings (Security, Policies, Locks), Cost Management, Monitoring, Automation....
 - A resource group can connect to resources in other resource groups. This scenario is common when two different resources are related but don't share the same lifecycle or access pattern. For example, you can have a web app that connects to a database in a different resource group.
 - When you delete a resource group, all resources in the resource group are also deleted.
 - The resources in a resource group can be located in different regions than the resource group. When you create a resource group, you need to provide a location for that resource group.
 - An Azure resource inherits locks from its resource group when you apply a lock at a parent scope, all resources within that scope inherit the same lock. Even resources you add later inherit the lock from the parent.
 - Resources don't inherit the tags you apply to a resource group or a subscription
 - All resources within a resource group will inherit the permissions set in the former

### Containers and VMs are isolated from host hardware

### Network peering - used to stablish communication between virtual networks (VNtes)

### Region Pairs:  allows you to replicate resources across a geography to ensure business continuity during a natural disaster at the primary site

### Peering:  allow resources on two different Azure virtual networks to communicate with each other

### Service Endipoints:  use it to connect Azure resources, such as Azure SQL databases, to an Azure virtual network

### Express Route
It is the same as AWS Direct Connect - connect customers local enterprise network with MS Azure directly thru a private exclusive connection (physical connection)

## Storage Services

<img width="695" alt="image" src="https://github.com/user-attachments/assets/88794d29-a7b9-4ebe-af2e-1d032218d8e7">

### Azure Storage
 - Locally redundant storage (LRS) - 11 9´s - 3 copies in the same DC
 - Zone-redundant storage (ZRS) - 12 9´s - 3 copies in 3 differente AZ´s (DC´s)
 - Geo-redundant storage (GRS) copies your data synchronously three times within a single physical location in the primary region using LRS. It then copies your data asynchronously to a single physical location in the secondary region. Within the secondary region, your data is copied synchronously three times using LRS. 16 9´s
 - Geo-zone-redundant storage (GZRS) copies your data synchronously across three Azure availability zones in the primary region using ZRS. It then copies your data asynchronously to a single physical location in the secondary region. Within the secondary region, your data is copied synchronously three times using LRS. 16 9´s

 - Blob Storage - block blob accounts: object storage :: kind of S3
      - Common use cases for Azure Blob storage:
      - serving images or documents directly to a browser;
      - storing data for backup and restore

The Archive storage tier stores data offline and offers the lowest storage costs, but also the highest costs to rehydrate and access data. The Hot storage tier is optimized for storing data that is accessed frequently. Data in the Cool access tier can tolerate slightly lower availability, but still requires high durability, retrieval latency, and throughput characteristics similar to hot data.

Review:  https://learn.microsoft.com/en-us/azure/storage/common/storage-redundancy 

 - Azure Files: it is a fully managed file shares in the cloud that are accessible via the industry-standard SMB and NFS protocols. Azure Files shares can be mounted concurrently by cloud or on-premises deployments of Windows, Linux, and macOS. Azure Files shares can also be cached on Windows Servers with Azure File Sync for fast access near where the data is being used.

 - AzCopy is a command-line utility designed for copying data to and from Microsoft Azure Blob, File, and Table storage. With AzCopy, you can migrate your data from the file system to Azure Storage, or vice versa, using simple commands and with optimal performance.

 - On MaC ::  it worked using ./azcopy - such as...:  ./azcopy cp /mysourcepath/ "https://my URL to access the container SAS" --recursive=true

 - Azure Storage Explorer - Upload, download, and manage Azure Storage blobs, files, queues, and tables, as well as Azure Data Lake Storage entities and Azure managed disks. Configure storage permissions and access controls, tiers, and rules.
        >> Download it and use it, it is really a easier way to friendly work with you cloud storage / disks / shared files / ...

### Azure Arc:   Secure, monitor, and govern infrastructure across your environments, including on-premises, other public clouds, and edge devices. There's no charge to start, just add your infrastructure and enjoy the views

### ARM - Azure Resource Manager
It is a management layer that accepts requests from any Azure tool or API and enables you to create, update, and delete resources in an Azure account. It is json based to create and manage resources - infrastructure as a code.

[Review ARM Official Documentation](https://azure.microsoft.com/en-us/get-started/azure-portal/resource-manager/)

$\color{orange}{\text{         ..... Orange Text Here ........ }}$

DIO Challenges:

https://github.com/alexandreborsato/lab-open-source.git/desafio.py
https://github.com/alexandreborsato/lab-open-source.git/desafio1.py
https://github.com/alexandreborsato/lab-open-source.git/desafio2.py
https://github.com/alexandreborsato/lab-open-source.git/desafio3.py

### Azure TCO - Total Cost of Ownership: https://azure.microsoft.com/en-us/pricing/tco/calculator/
### Azure pricing calculator:  https://azure.microsoft.com/en-us/pricing/calculator/

### MS Azure App Services
It is used to Create, build, deploy, and manage powerful web, mobile, and API apps for employees or customers using a single back-end. Build standards-based web apps and APIs using .NET, Java, Node.js, PHP, and Python

### MS Azure Function Services
It lets you group functions as a logical unit for easier management, deployment and sharing of resources. Functions lets you execute your code in a serverless environment without having to first create a VM or publish a web application.

### Azure Virtual Machines (VMs):
Virtual machine workloads that are used only during certain periods, but you run them every hour of every day, then you are wasting money. These virtual machines are great candidates to deallocate when not in use and start back when required to save compute costs while the virtual machines are deallocated.

### Azure Virtual Desktop
Kind of workspace / virtual desktop - Easily scale your VM deployment. Create host pools to easily manage assignments, application groups, and settings for your entire organization

### MS Entra ID - It is the old MS AD - used to user and resources authentication. It is also a way for SSO.
 - Authentication, Authorization, MFA..., RBAC - Role Based Access Control, Conditional Access, B2B External Entra ID
 - MS Defender - it monitors security threats, can detect and block malware, provides security advisory
 - Azure Resource Manager
 - Zero trust - start from no access and add as per explicit requirement
 - Users are permanently deleted after 30 days they were deleted

<img width="455" alt="image" src="https://github.com/user-attachments/assets/d7dd32b5-290c-412f-826f-57ad56ef66a0">

### Management groups:
It can be used in environments that have multiple subscriptions to streamline the application of governance conditions
Use it to manage access, policies, and compliance across multiple subscriptions.

### Azure CLI::  https://learn.microsoft.com/en-us/cli/azure/?view=azure-cli-latest 

### Microsoft Purview
It is a family of data governance, risk, and compliance solutions that helps you get a single, unified view into your data. Microsoft Purview brings insights about your on-premises, multicloud, and software-as-a-service data together.

With Microsoft Purview, you can stay up-to-date on your data landscape thanks to:

 - Automated data discovery
 - Sensitive data classification
 - End-to-end data lineage*
   (*) Data lineage includes the data origin, what happens to it, and where it moves over time. Data lineage provides visibility and simplifies tracing errors back to the root cause in a data analytics process
 - Data Police is the feature in the Microsoft Purview governance portal used to manage access to data sources and datasets

### Security:
   Conditional Access is a feature that Microsoft Entra uses to allow or deny access to resources based on identity signals, such as the device being used. SSO enables a user to sign in one time and use that credential to access multiple resources and applications from different providers. MFA is a process whereby a user is prompted during the sign-in process for an additional form of identification. Hybrid identity solutions create a common user identity for authentication and authorization to all resources, regardless of location.
   Azure RBAC role is applied to a scope, which is a resource or set of resources that the access applies to. Resource locks prevent the accidental change or deletion of a resource. Resource tags are used to locate and act on resources associated with specific workloads, environments, business units, and owners. Policies enforce different rules across resource configurations so that the configurations stay compliant with corporate standards.
   
### Azure Policy
It is a service in Azure that enables you to create, assign, and manage policies that control or audit your resources. These policies enforce different rules across your resource configurations so that those configurations stay compliant with corporate standards

### MS Services Trust Portal::  https://servicetrust.microsoft.com/

### Azure Advisor: kind of recomendation center / insights to address issues with:
 - Reliability
 - Security
 - Performance
 - Costs
 - Operational Excellence
 -   >> for example, it sends notifications when there are new recommendations for reducing Azure costs

### Azure Monitor - It monitors and provide insights about resources such as VMs, Storages, apps, ... it is possible to create alerts, review metrics, check for services health...

 - Health Advisories: use it to proactively review and act on to avoid service interruptions, such as service retirements and breaking changes
    >> Health advisories are issues that require that you take proactive action to avoid service interruptions, such as service retirements and breaking changes. Service issues are problems such as outages that require immediate actions

### Azure Service Health - it notifies you about Azure service incidents and planned maintenance so you can take action to mitigate downtime. Configure customizable cloud alerts and use your personalized dashboard to analyze health issues, monitor the impact to your cloud resources, get guidance and support, and share details and updates. Use it to review the root cause analysis (RCA) report for a service outage that occurred. Configurable cloud alerts notify you about active and upcoming service issues

### Application Insights is a feature of Azure Monitor that allows you to monitor running applications, automatically detect performance anomalies, and use built-in analytics tools to see what users do on an app

### Azure resource lock
It prevents resources from being accidentally deleted or changed. Review before locking and take care. It is possible to set the lock for read-only or for delete. When set for delete, the resource can be read, changed, moved,... but cannot be deleted. When set to read-only, it can only be read and just it.

Even with Azure role-based access control (Azure RBAC) policies in place, there's still a risk that people with the right level of access could delete critical cloud resources. Resource locks prevent resources from being deleted or updated, depending on the type of lock. Resource locks can be applied to individual resources, resource groups, or even an entire subscription. Resource locks are inherited, meaning that if you place a resource lock on a resource group, all of the resources within the resource group will also have the resource lock applied. In the case of lock inherited from a resource group, you can move a specific resource to another resource group that doesn´t have a lock and so the lock will not apply anylonger. However, if the lock is set directly to a specific resource, even when moving to a another resource group, the lock will be moved alongside with the resource. Warning:::  it the lock is a read-only, it is not possible to move the resource at all.

### Support Plans:

<img width="994" alt="image" src="https://github.com/user-attachments/assets/346a393c-7ae8-4fb9-8ce9-af3c32cd0498">



<img width="360" alt="image" src="https://github.com/user-attachments/assets/2920ee53-3169-42b5-b267-bb4c95ac5a98">
