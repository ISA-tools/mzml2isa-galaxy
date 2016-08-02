import sys
import json
import os
from mzml2isa.parsing import full_parse
# import progressbar as pb


USERMETA = {'characteristics':           {'organism': {'name':'', 'accession':'', 'ref':''},
                                          'organism_variant':  {'name':'', 'accession':'', 'ref':''},
                                          'organism_part':     {'name':'', 'accession':'', 'ref':''},
                                         },
            'investigation':             {'identifier': '', 'title': 'Investigation', 'description': '',
                                          'submission_date':'', 'release_date':''
                                         },
            'investigation_publication': {'pubmed': '', 'doi': '', 'author_list': '', 'title':'',
                                          'status': {'name':'', 'accession':'', 'ref':'PSO'},
                                         },

            'study':                     {
                                          'title': '', 'description': '', 'submission_date':'', 'release_date':'',
                                         },
            'study_publication':         {'pubmed': '', 'doi': '', 'author_list': '', 'title':'',
                                          'status': {'name':'', 'accession':'', 'ref':'PSO'},
                                         },

            'description':               {'sample_collect':'', 'extraction':'', 'chroma':'', 'mass_spec':'',
                                          'data_trans':'', 'metabo_id':''
                                         },

            #Multiple Values Parameters
            'study_contacts':            [
                                            {'first_name': '', 'last_name': '', 'mid':'', 'email':'',
                                             'fax': '', 'phone':'', 'adress':'', 'affiliation':'',
                                             'roles': {'name':'', 'accession':'', 'ref':''},
                                            },
                                         ],

            'investigation_contacts':    [
                                            {'first_name': '', 'last_name': '', 'mid':'', 'email':'',
                                             'fax': '', 'phone':'', 'adress':'', 'affiliation':'',
                                             'roles': {'name':'', 'accession':'', 'ref':''},
                                            },
                                         ],

            'Post Extraction':           {'value': ''},
            'Derivatization':            {'value': ''},
            'Chromatography Instrument': {'name':'', 'ref':'', 'accession':''},
            'Column type':               {'value': ''},
            'Column model':              {'value': ''},
}


# Parse
def pop_dict(inlist, USERMETA, study_title):

    # study info
    s_submission_date = inlist[6]
    s_release_date = inlist[7]
    s_description = inlist[8]
    s_publication = inlist[9]
    s_doi = inlist[10]
    s_title = inlist[11]
    s_status = inlist[12]
    s_author = inlist[13]

    # study contact info
    s_first_name = inlist[14]
    s_mid_initials = inlist[15]
    s_last_name = inlist[16]
    s_telephone = inlist[17]
    s_fax = inlist[18]
    s_affiliation = inlist[19]
    s_role = inlist[20]
    s_mail = inlist[21]
    s_address = inlist[22]

    # investigation info
    i_submission_date = inlist[23]
    i_release_date = sys.argv[24]
    i_description = sys.argv[25]
    i_publication = sys.argv[26]
    i_doi = sys.argv[27]
    i_title = sys.argv[28]
    i_status = sys.argv[29]
    i_author = sys.argv[30]

    # investigation contact info
    i_first_name = sys.argv[31]
    i_mid_initials = sys.argv[32]
    i_last_name = sys.argv[33]
    i_telephone = sys.argv[34]
    i_fax = sys.argv[35]
    i_affiliation = sys.argv[36]
    i_role = sys.argv[37]
    i_mail = sys.argv[38]
    i_address = sys.argv[39]

    # organism info
    organism_text = sys.argv[40]
    organism_ref = sys.argv[41]
    organism_iri = sys.argv[42]
    organism_variant_text = sys.argv[43]
    organism_variant_ref = sys.argv[44]
    organism_variant_iri = sys.argv[45]
    organism_part_text = sys.argv[46]
    organism_part_ref = sys.argv[47]
    organism_part_iri = sys.argv[48]

    # Fill in USERMETA dictionary
    USERMETA['characteristics']['organism']['value'] = organism_text
    USERMETA['characteristics']['organism']['accession'] = organism_iri
    USERMETA['characteristics']['organism']['ref'] = organism_ref

    USERMETA['characteristics']['organism_variant']['value'] = organism_variant_text
    USERMETA['characteristics']['organism_variant']['accession'] = organism_variant_iri
    USERMETA['characteristics']['organism_variant']['ref'] = organism_variant_ref

    USERMETA['characteristics']['organism_part']['value'] = organism_part_text
    USERMETA['characteristics']['organism_part']['accession'] = organism_part_iri
    USERMETA['characteristics']['organism_part']['ref'] = organism_part_ref

    #USERMETA['investigation']['identifier'] = # uses study identifier
    USERMETA['investigation']['description'] = i_description
    USERMETA['investigation']['submission_date'] = i_submission_date
    USERMETA['investigation']['release_date'] = i_release_date

    USERMETA['investigation_publication']['pubmed'] = i_publication
    USERMETA['investigation_publication']['author_list'] = i_author
    USERMETA['investigation_publication']['title'] = i_title
    USERMETA['investigation_publication']['doi'] = i_doi
    USERMETA['investigation_publication']['status']['name'] = i_status
    USERMETA['investigation_publication']['status']['accession'] = ""

    USERMETA['investigation_contacts'][0]['first_name'] = i_first_name
    USERMETA['investigation_contacts'][0]['last_name'] = i_last_name
    USERMETA['investigation_contacts'][0]['mid'] = i_mid_initials
    USERMETA['investigation_contacts'][0]['email'] = i_mail
    USERMETA['investigation_contacts'][0]['fax'] = i_fax
    USERMETA['investigation_contacts'][0]['phone'] = i_telephone
    USERMETA['investigation_contacts'][0]['adress'] = i_address
    USERMETA['investigation_contacts'][0]['affiliation'] = i_affiliation
    USERMETA['investigation_contacts'][0]['roles']['name'] = i_role
    USERMETA['investigation_contacts'][0]['roles']['accession'] = ""

    USERMETA['study']['title'] = study_title
    USERMETA['study']['description'] = s_description
    USERMETA['study']['submission_date'] = s_submission_date
    USERMETA['study']['release_date'] = s_release_date

    USERMETA['study_publication']['pubmed'] = s_publication
    USERMETA['study_publication']['author_list'] = s_author
    USERMETA['study_publication']['title'] = s_title
    USERMETA['study_publication']['doi'] = s_doi
    USERMETA['study_publication']['status']['name'] = s_status
    USERMETA['study_publication']['status']['accession'] = ""

    USERMETA['study_contacts'][0]['first_name'] = s_first_name
    USERMETA['study_contacts'][0]['last_name'] = s_last_name
    USERMETA['study_contacts'][0]['mid'] = s_mid_initials
    USERMETA['study_contacts'][0]['email'] = s_mail
    USERMETA['study_contacts'][0]['fax'] = s_fax
    USERMETA['study_contacts'][0]['phone'] = s_telephone
    USERMETA['study_contacts'][0]['adress'] = s_address
    USERMETA['study_contacts'][0]['affiliation'] = s_affiliation
    USERMETA['study_contacts'][0]['roles']['name'] = s_role
    USERMETA['study_contacts'][0]['roles']['accession'] = ""

    return USERMETA

# General
inlist = sys.argv
inputzip = inlist[1]
jsontxt = inlist[2]
html_file = inlist[3]
out_dir = inlist[4]
study_title = inlist[5]

# check if using json file
if os.path.isfile(jsontxt):
    with open(jsontxt, 'r') as f:
        usermeta = json.load(f)
else:
    print inlist
    usermeta = pop_dict(inlist, USERMETA, study_title)

# parse the files
full_parse(inputzip, out_dir, study_title, usermeta=usermeta, split=True, merge=False, verbose=False, multip=False)



html_code = '<a href="%s/a_%s_metabolite_profiling_mass_spectrometry.txt">a_%s_metabolite_profiling_mass_spectrometry.txt</a><br/><a href="%s/i_Investigation.txt">i_Investigation.txt</a><br/><a href="%s/s_%s.txt">s_test.txt</a><br/>' % tuple([study_title]*6)

with open(html_file, 'wb') as f:
    f.write(html_code)


