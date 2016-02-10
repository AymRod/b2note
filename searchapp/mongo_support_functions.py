import json, bson



from .models import *


def DeleteFromPOSTinfo( db_id ):
    """
      Function: DeleteFromPOSTinfo
      ----------------------------
        Removes an annotation from MongoDB.
        
        params:
            db_id (str): ID of the document to remove.
        
        returns:
            bool: True if successful, False otherwise.
    """
    del_flag = False
    try:
        if db_id and type(db_id) is unicode and len(db_id)>0:
            Annotation.objects.get(id=db_id).delete()
            del_flag = True
        else:
            print "Argument provided is not a valid collection document id"
    except ValueError:
        pass

    if del_flag:
        print "Removed an Annotation from DB"
        return True

    print "Could not remove from DB"
    return False


def CreateFromPOSTinfo( subject_url, object_json ):
    """
      Function: CreateFromPOSTinfo
      ----------------------------
        Creates an annotation in MongoDB.
        
        params:
            subject_url (str): URL of the annotation to create.
            object_json (str): JSON of the annotation provided by SOLR
        
        returns:
            bool: True if successful, False otherwise.
    """
    object_uri   = ""
    object_label = ""

    try:

        if subject_url and type(subject_url) is unicode and len(subject_url)>0:

            o = json.loads(object_json)

            if "uris" in o.keys():
                object_uri = o["uris"][0]
                if "labels" in o.keys(): object_label = o["labels"]

                print object_label, " ", object_uri

                ann = Annotation(\
                        triple=Triple(\
                                subject=TripleElement(iri=subject_url,label="", definition="",curation_status="", ontology_iri="",ontology_shortname="",ontology_version="",),\
                                predicate=TripleElement(iri="http://purl.obolibrary.org/obo/IAO_0000136",label="is about",definition="Is_about is a (currently) primitive relation that relates an information artifact to an entity.",curation_status="pending final vetting",ontology_iri="http://purl.obolibrary.org/obo/iao.owl",ontology_shortname="IAO",ontology_version="2015,02,23",),\
                                object=TripleElement(\
                                        iri     =   object_uri,\
                                        label   =   object_label,\
                                        definition = "",\
                                        curation_status = "",\
                                        ontology_iri = "",\
                                        ontology_shortname= "",\
                                        ontology_version= "",\
                                ),\
                        ),\
                        provenance=Provenance(\
                                createdBy="abremaud@esciencefactory.com",
                        ),\
                ).save()

    except ValueError:

        print "Could not save to DB"
        return False

    print "Created an Annotation"
    return True
