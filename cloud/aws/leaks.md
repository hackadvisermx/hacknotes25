

```
castr@mymac ~ % aws s3 ls s3://congreso-gto --no-sign-request
                           PRE /
                           PRE acuerdos/
                           PRE armonizacion/
                           PRE ckan/
                           PRE ckeditor_assets/
                           PRE comites/
                           PRE congreso-gto/
                           PRE contraloria/
                           PRE db/
                           PRE disposiciones/
                           PRE https:/
                           PRE indicadores/
                           PRE informes-mensuales/
                           PRE iniciativadigital/
                           PRE multimedia/
                           PRE normatividad-interna/
                           PRE observatorioCiudadano/
                           PRE resumenes/
                           PRE transparencia/
                           PRE uploads/
                           PRE uploads_v2/
castr@mymac ~ %
```

```
aws s3 ls s3://redlei/ --no-sign-request
```


```
https://elconta.mx/

castr@mymac ~ % aws s3 ls s3://elconta/ --no-sign-request
                           PRE Administracion/
                           PRE cursos/
                           PRE ebooks/
                           PRE leyes/
                           PRE programas/
                           PRE revistas/
                           PRE sites_backups/
                           PRE temporales/
                           PRE videos/
castr@mymac ~ %
```

```
 aws s3 ls s3://app-assets-prod/ --no-sign-request
 aws s3 ls s3://idea-documents/ --no-sign-request
 ✗ aws s3 ls s3://store.development/frs/22_FW_Dior/ --no-sign-request
 aws s3 ls s3://idea-assets-dev/projects/ --no-sign-request
 aws s3 ls s3://idea-assets-prod/ --no-sign-request --recursive
 aws s3 ls s3://content-partners/ --no-sign-request --recursive
```


```
aws s3 ls --no-sign-request s3://ford-dataset
aws s3api get-bucket-ownership-controls --no-sign-request --bucket ford-dataset
aws s3api get-object-acl --no-sign-request --bucket ford-dataset --key poc.txt


aws s3api get-object-acl --no-sign-request --bucket ford-dataset --key device_22_2021_01_11_13_12_42.jpg
{
    "Owner": {
        "DisplayName": "rahim",
        "ID": "e82fef7980715f731b29d89a29f4f79935f046f080b06b38d144fe4ffc77240b"
    },
    "Grants": [
        {
            "Grantee": {
                "DisplayName": "rahim",
                "ID": "e82fef7980715f731b29d89a29f4f79935f046f080b06b38d144fe4ffc77240b",
                "Type": "CanonicalUser"
            },
            "Permission": "FULL_CONTROL"
        }
    ]
}


aws s3api get-bucket-acl --no-sign-request --bucket ford-dataset


{
    "Owner": {
        "DisplayName": "rahim",
        "ID": "e82fef7980715f731b29d89a29f4f79935f046f080b06b38d144fe4ffc77240b"
    },
    "Grants": [
        {
            "Grantee": {
                "DisplayName": "rahim",
                "ID": "e82fef7980715f731b29d89a29f4f79935f046f080b06b38d144fe4ffc77240b",
                "Type": "CanonicalUser"
            },
            "Permission": "FULL_CONTROL"
        },
        {
            "Grantee": {
                "Type": "Group",
                "URI": "http://acs.amazonaws.com/groups/global/AllUsers"
            },
            "Permission": "READ"
        },
        {
            "Grantee": {
                "Type": "Group",
                "URI": "http://acs.amazonaws.com/groups/global/AllUsers"
            },
            "Permission": "READ_ACP"
        },
        {
            "Grantee": {
                "Type": "Group",
                "URI": "http://acs.amazonaws.com/groups/global/AuthenticatedUsers"
            },
            "Permission": "READ"
        },
        {
            "Grantee": {
                "Type": "Group",
                "URI": "http://acs.amazonaws.com/groups/global/AuthenticatedUsers"
            },
            "Permission": "READ_ACP"
        },
        {
            "Grantee": {
                "Type": "Group",
                "URI": "http://acs.amazonaws.com/groups/s3/LogDelivery"
            },
            "Permission": "FULL_CONTROL"
        }
    ]
}

aws s3api get-bucket-policy --no-sign-request --bucket ford-dataset
aws s3api get-bucket-policy-status --no-sign-request --bucket ford-dataset
aws s3api get-bucket-notification-configuration --no-sign-request --bucket ford-dataset
aws s3api get-bucket-logging --no-sign-request --bucket ford-dataset
aws s3api get-bucket-cors --no-sign-request --bucket ford-dataset


aws s3api list-objects  --no-sign-request --bucket ford-dataset



```

## Recursos
- https://github.com/WeAreCloudar/s3-account-search
- https://github.com/sa7mon/S3Scanner
- 