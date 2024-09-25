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

### MS Azure App Services
It is used to Create, build, deploy, and manage powerful web, mobile, and API apps for employees or customers using a single back-end. Build standards-based web apps and APIs using .NET, Java, Node.js, PHP, and Python

### MS Azure Function Services
It lets you group functions as a logical unit for easier management, deployment and sharing of resources. Functions lets you execute your code in a serverless environment without having to first create a VM or publish a web application.

### Azure Virtual Desktop
Kind of workspace / virtual desktop - Easily scale your VM deployment. Create host pools to easily manage assignments, application groups, and settings for your entire organization

### Microsoft Purview
It is a family of data governance, risk, and compliance solutions that helps you get a single, unified view into your data. Microsoft Purview brings insights about your on-premises, multicloud, and software-as-a-service data together.

With Microsoft Purview, you can stay up-to-date on your data landscape thanks to:

Automated data discovery
Sensitive data classification
End-to-end data lineage

### Azure Policy
It is a service in Azure that enables you to create, assign, and manage policies that control or audit your resources. These policies enforce different rules across your resource configurations so that those configurations stay compliant with corporate standards

### Azure resource lock
It prevents resources from being accidentally deleted or changed.

Even with Azure role-based access control (Azure RBAC) policies in place, there's still a risk that people with the right level of access could delete critical cloud resources. Resource locks prevent resources from being deleted or updated, depending on the type of lock. Resource locks can be applied to individual resources, resource groups, or even an entire subscription. Resource locks are inherited, meaning that if you place a resource lock on a resource group, all of the resources within the resource group will also have the resource lock applied.

![image](https://github.com/user-attachments/assets/fdeac407-c397-4fe0-be5c-22be71a0847e)

