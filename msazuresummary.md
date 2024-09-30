# MS Azure Summary

### Resource Groups
It is used to group resources as a project/ptogram or architecture, environment. Here you can create your cloud resources.
The reources are VMs, DBs, virtual networks...
Within the Resource Groups there are some features and configurations to be exploired such as Activity Log, IAM (permissions), Tags, Settings (Security, Policies, Locks), Cost Management, Monitoring, Automation....

### Containers and VMs are isolated from host hardware

### Network peering - used to stablish communication between virtual networks (VNtes)

### Express Route
It is the same as AWS Direct Connect - connect customers local enterprise network with MS Azure directly thru a private exclusive connection (physical connection)

## Storage Services

<img width="695" alt="image" src="https://github.com/user-attachments/assets/88794d29-a7b9-4ebe-af2e-1d032218d8e7">

### Azure Storage
 - Locally redundant storage (LRS) - 11 9´s - 3 copies in the same DC
 - Zone-redundant storage (ZRS) - 12 9´s - 3 copies in 3 differente AZ´s (DC´s)
 - Geo-redundant storage (GRS) copies your data synchronously three times within a single physical location in the primary region using LRS. It then copies your data asynchronously to a single physical location in the secondary region. Within the secondary region, your data is copied synchronously three times using LRS. 16 9´s
 - Geo-zone-redundant storage (GZRS) copies your data synchronously across three Azure availability zones in the primary region using ZRS. It then copies your data asynchronously to a single physical location in the secondary region. Within the secondary region, your data is copied synchronously three times using LRS. 16 9´s

block blob accounts: object storage 0 kind of S3

Review:  https://learn.microsoft.com/en-us/azure/storage/common/storage-redundancy 

 - Azure Files: it is a fully managed file shares in the cloud that are accessible via the industry-standard SMB and NFS protocols. Azure Files shares can be mounted concurrently by cloud or on-premises deployments of Windows, Linux, and macOS. Azure Files shares can also be cached on Windows Servers with Azure File Sync for fast access near where the data is being used.

 - AzCopy is a command-line utility designed for copying data to and from Microsoft Azure Blob, File, and Table storage. With AzCopy, you can migrate your data from the file system to Azure Storage, or vice versa, using simple commands and with optimal performance.

 - On MaC ::  it worked using ./azcopy - such as...:  ./azcopy cp /mysourcepath/ "https://my URL to access the container SAS" --recursive=true

 - Azure Storage Explorer - Upload, download, and manage Azure Storage blobs, files, queues, and tables, as well as Azure Data Lake Storage entities and Azure managed disks. Configure storage permissions and access controls, tiers, and rules.
        >> Download it and use it, it is really a easier way to friendly work with you cloud storage / disks / shared files / ...

### Azure Arc:   Secure, monitor, and govern infrastructure across your environments, including on-premises, other public clouds, and edge devices. There's no charge to start, just add your infrastructure and enjoy the views

### ARM - Azure Resource Manager - json based to create and manage resources - infrastructure as a code.
[Review ARM Official Documentation](https://azure.microsoft.com/pt-br/get-started/azure-portal/resource-manager) 
<img width="146" alt="image" src="https://github.com/user-attachments/assets/47d808e6-c8f7-4de0-baf4-bc8b3f1f3646">

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

### Azure Virtual Desktop
Kind of workspace / virtual desktop - Easily scale your VM deployment. Create host pools to easily manage assignments, application groups, and settings for your entire organization

### MS Entra ID - It is the old MS AD - used to user and resources authentication. It is also a way for SSO.
 - Authentication, Authorization, MFA..., RBAC - Role Based Access Control, Conditional Access, B2B External Entra ID
 - MS Defender - it monitors security threats, can detect and block malware, provides security advisory
 - Azure Resource Manager
 - Zero trust - start from no access and add as per explicit requirement
 - Users are permanently deleted after 30 days they were deleted

<img width="455" alt="image" src="https://github.com/user-attachments/assets/d7dd32b5-290c-412f-826f-57ad56ef66a0">

### Azure CLI::  https://learn.microsoft.com/en-us/cli/azure/?view=azure-cli-latest 

### Microsoft Purview
It is a family of data governance, risk, and compliance solutions that helps you get a single, unified view into your data. Microsoft Purview brings insights about your on-premises, multicloud, and software-as-a-service data together.

With Microsoft Purview, you can stay up-to-date on your data landscape thanks to:

 - Automated data discovery
 - Sensitive data classification
 - End-to-end data lineage*
   (*) Data lineage includes the data origin, what happens to it, and where it moves over time. Data lineage provides visibility and simplifies tracing errors back to the root cause in a data analytics process

### Azure Policy
It is a service in Azure that enables you to create, assign, and manage policies that control or audit your resources. These policies enforce different rules across your resource configurations so that those configurations stay compliant with corporate standards

### MS Services Trust Portal::  https://servicetrust.microsoft.com/

### Azure resource lock
It prevents resources from being accidentally deleted or changed. Review before locking and take care. It is possible to set the lock for read-only or for delete. When set for delete, the resource can be read, changed, moved,... but cannot be deleted. When set to read-only, it can only be read and just it.

Even with Azure role-based access control (Azure RBAC) policies in place, there's still a risk that people with the right level of access could delete critical cloud resources. Resource locks prevent resources from being deleted or updated, depending on the type of lock. Resource locks can be applied to individual resources, resource groups, or even an entire subscription. Resource locks are inherited, meaning that if you place a resource lock on a resource group, all of the resources within the resource group will also have the resource lock applied. In the case of lock inherited from a resource group, you can move a specific resource to another resource group that doesn´t have a lock and so the lock will not apply anylonger. However, if the lock is set directly to a specific resource, even when moving to a another resource group, the lock will be moved alongside with the resource. Warning:::  it the lock is a read-only, it is not possible to move the resource at all.

<img width="360" alt="image" src="https://github.com/user-attachments/assets/2920ee53-3169-42b5-b267-bb4c95ac5a98">
