## Splunk

Splunk is a software platform widely used for **monitoring, searching, analyzing and visualizing the machine-generated data in real time**. It performs capturing, indexing, and correlating the real time data in a searchable container and produces graphs, alerts, dashboards and visualizations

## Splunk Components

### **Splunk Forwarder**

Splunk Forwarder is a lightweight agent installed on the endpoint intended to be monitored, and its main task is to collect the data and send it to the Splunk instance. It does not affect the endpoint's performance as it takes very few resources to process. Some of the key data sources are:

-   Web server generating web traffic.
-   Windows machine generating Windows Event Logs, PowerShell, and Sysmon data.
-   Linux host generating host-centric logs.
-   Database generating DB connection requests, responses, and errors

### **Splunk Indexer**  

Splunk Indexer plays the main role in processing the data it receives from forwarders. It takes the data, normalizes it into field-value pairs, determines the datatype of the data, and stores them as events. Processed data is easy to search and analyze.

### **Search Head**

Splunk Search Head is the place within the Search & Reporting App where users can search the indexed logs as shown below. When the user searches for a term or uses a Search language known as Splunk Search Processing Language, the request is sent to the indexer and the relevant events are returned in the form of field-value pairs.

### **Splunk Dashboard**

The last section is the **Home Dashboard**. By default, no dashboards are displayed. You can choose from a range of dashboards readily available within your Splunk instance. You can select a dashboard from the dropdown menu or by visiting the **dashboards listing page**.

## REferencias 
- https://tryhackme.com/room/splunk101
- https://docs.splunk.com/Documentation
- 