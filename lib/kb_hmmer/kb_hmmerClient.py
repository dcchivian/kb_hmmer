# -*- coding: utf-8 -*-
############################################################
#
# Autogenerated by the KBase type compiler -
# any changes made here will be overwritten
#
############################################################

from __future__ import print_function
# the following is a hack to get the baseclient to import whether we're in a
# package or not. This makes pep8 unhappy hence the annotations.
try:
    # baseclient and this client are in a package
    from .baseclient import BaseClient as _BaseClient  # @UnusedImport
except ImportError:
    # no they aren't
    from baseclient import BaseClient as _BaseClient  # @Reimport


class kb_hmmer(object):

    def __init__(
            self, url=None, timeout=30 * 60, user_id=None,
            password=None, token=None, ignore_authrc=False,
            trust_all_ssl_certificates=False,
            auth_svc='https://ci.kbase.us/services/auth/api/legacy/KBase/Sessions/Login'):
        if url is None:
            raise ValueError('A url is required')
        self._service_ver = None
        self._client = _BaseClient(
            url, timeout=timeout, user_id=user_id, password=password,
            token=token, ignore_authrc=ignore_authrc,
            trust_all_ssl_certificates=trust_all_ssl_certificates,
            auth_svc=auth_svc)

    def HMMER_MSA_Search(self, params, context=None):
        """
        Method for HMMER search of an MSA against many sequences 
        **
        **    overloading as follows:
        **        input_msa_ref: MSA
        **        input_many_ref: SequenceSet, FeatureSet, Genome, GenomeSet
        **        output_name: SequenceSet (if input_many is SequenceSet), (else) FeatureSet
        :param params: instance of type "HMMER_Params" (HMMER Input Params)
           -> structure: parameter "workspace_name" of type "workspace_name"
           (** The workspace object refs are of form: ** **    objects =
           ws.get_objects([{'ref':
           params['workspace_id']+'/'+params['obj_name']}]) ** ** "ref" means
           the entire name combining the workspace id and the object name **
           "id" is a numerical identifier of the workspace or object, and
           should just be used for workspace ** "name" is a string identifier
           of a workspace or object.  This is received from Narrative.),
           parameter "input_many_ref" of type "data_obj_ref", parameter
           "input_msa_ref" of type "data_obj_ref", parameter
           "output_filtered_name" of type "data_obj_name", parameter
           "genome_disp_name_config" of String, parameter "e_value" of
           Double, parameter "bitscore" of Double, parameter "model_cov_perc"
           of Double, parameter "maxaccepts" of Double
        :returns: instance of type "HMMER_Output" (HMMER Output) ->
           structure: parameter "report_name" of type "data_obj_name",
           parameter "report_ref" of type "data_obj_ref"
        """
        return self._client.call_method('kb_hmmer.HMMER_MSA_Search',
                                        [params], self._service_ver, context)

    def HMMER_Local_MSA_Group_Search(self, params, context=None):
        """
        Method for HMMER search of a Local MSA Group (found automatically within workspace) against many sequences 
        **
        **    overloading as follows:
        **        input_many_ref: SequenceSet, FeatureSet, Genome, GenomeSet
        **        output_name: SequenceSet (if input_many is SequenceSet), (else) FeatureSet
        :param params: instance of type "HMMER_Local_MSA_Group_Params" (HMMER
           Local MSA Group Input Params) -> structure: parameter
           "workspace_name" of type "workspace_name" (** The workspace object
           refs are of form: ** **    objects = ws.get_objects([{'ref':
           params['workspace_id']+'/'+params['obj_name']}]) ** ** "ref" means
           the entire name combining the workspace id and the object name **
           "id" is a numerical identifier of the workspace or object, and
           should just be used for workspace ** "name" is a string identifier
           of a workspace or object.  This is received from Narrative.),
           parameter "input_msa_refs" of type "data_obj_ref", parameter
           "input_many_ref" of type "data_obj_ref", parameter
           "output_filtered_name" of type "data_obj_name", parameter
           "genome_disp_name_config" of String, parameter "coalesce_output"
           of type "bool", parameter "e_value" of Double, parameter
           "bitscore" of Double, parameter "model_cov_perc" of Double,
           parameter "maxaccepts" of Double, parameter "heatmap" of type
           "bool", parameter "low_val" of type "bool", parameter "vertical"
           of type "bool", parameter "show_blanks" of type "bool"
        :returns: instance of type "HMMER_Output" (HMMER Output) ->
           structure: parameter "report_name" of type "data_obj_name",
           parameter "report_ref" of type "data_obj_ref"
        """
        return self._client.call_method('kb_hmmer.HMMER_Local_MSA_Group_Search',
                                        [params], self._service_ver, context)

    def HMMER_dbCAN_Search(self, params, context=None):
        """
        Method for HMMER search of dbCAN Markov Models of CAZy families
        **
        **    overloading as follows:
        **        input_many_ref: SequenceSet, FeatureSet, Genome, GenomeSet
        **        output_name: SequenceSet (if input_many is SequenceSet), (else) FeatureSet
        :param params: instance of type "HMMER_dbCAN_Params" (HMMER dbCAN
           Input Params) -> structure: parameter "workspace_name" of type
           "workspace_name" (** The workspace object refs are of form: ** ** 
           objects = ws.get_objects([{'ref':
           params['workspace_id']+'/'+params['obj_name']}]) ** ** "ref" means
           the entire name combining the workspace id and the object name **
           "id" is a numerical identifier of the workspace or object, and
           should just be used for workspace ** "name" is a string identifier
           of a workspace or object.  This is received from Narrative.),
           parameter "input_dbCAN_AA_ids" of type "data_obj_ref", parameter
           "input_dbCAN_CBM_ids" of type "data_obj_ref", parameter
           "input_dbCAN_CE_ids" of type "data_obj_ref", parameter
           "input_dbCAN_GH_ids" of type "data_obj_ref", parameter
           "input_dbCAN_GT_ids" of type "data_obj_ref", parameter
           "input_dbCAN_PL_ids" of type "data_obj_ref", parameter
           "input_dbCAN_cellulosome_ids" of type "data_obj_ref", parameter
           "input_many_ref" of type "data_obj_ref", parameter
           "output_filtered_name" of type "data_obj_name", parameter
           "genome_disp_name_config" of String, parameter "coalesce_output"
           of type "bool", parameter "save_ALL_featureSets" of type "bool",
           parameter "e_value" of Double, parameter "bitscore" of Double,
           parameter "model_cov_perc" of Double, parameter "maxaccepts" of
           Double, parameter "heatmap" of type "bool", parameter "low_val" of
           type "bool", parameter "vertical" of type "bool", parameter
           "show_blanks" of type "bool"
        :returns: instance of type "HMMER_Output" (HMMER Output) ->
           structure: parameter "report_name" of type "data_obj_name",
           parameter "report_ref" of type "data_obj_ref"
        """
        return self._client.call_method('kb_hmmer.HMMER_dbCAN_Search',
                                        [params], self._service_ver, context)

    def HMMER_EnvBioelement_Search(self, params, context=None):
        """
        Method for HMMER search of Markov Models of environmental bioelement families
        **
        **    overloading as follows:
        **        input_many_ref: SequenceSet, FeatureSet, Genome, GenomeSet
        **        output_name: SequenceSet (if input_many is SequenceSet), (else) FeatureSet
        :param params: instance of type "HMMER_EnvBioelement_Params" (HMMER
           EnvBioelement Input Params) -> structure: parameter
           "workspace_name" of type "workspace_name" (** The workspace object
           refs are of form: ** **    objects = ws.get_objects([{'ref':
           params['workspace_id']+'/'+params['obj_name']}]) ** ** "ref" means
           the entire name combining the workspace id and the object name **
           "id" is a numerical identifier of the workspace or object, and
           should just be used for workspace ** "name" is a string identifier
           of a workspace or object.  This is received from Narrative.),
           parameter "input_env-bioelement_N_ids" of type "data_obj_ref",
           parameter "input_env-bioelement_S_ids" of type "data_obj_ref",
           parameter "input_env-bioelement_O_ids" of type "data_obj_ref",
           parameter "input_env-bioelement_CH4_ids" of type "data_obj_ref",
           parameter "input_env-bioelement_CFix_ids" of type "data_obj_ref",
           parameter "input_env-bioelement_CMono_ids" of type "data_obj_ref",
           parameter "input_env-bioelement_C1_ids" of type "data_obj_ref",
           parameter "input_env-bioelement_H_ids" of type "data_obj_ref",
           parameter "input_env-bioelement_Halo_ids" of type "data_obj_ref",
           parameter "input_env-bioelement_As_ids" of type "data_obj_ref",
           parameter "input_env-bioelement_Se_ids" of type "data_obj_ref",
           parameter "input_env-bioelement_Ur_ids" of type "data_obj_ref",
           parameter "input_env-bioelement_Me_ids" of type "data_obj_ref",
           parameter "input_env-bioelement_CN_ids" of type "data_obj_ref",
           parameter "input_many_ref" of type "data_obj_ref", parameter
           "output_filtered_name" of type "data_obj_name", parameter
           "genome_disp_name_config" of String, parameter "coalesce_output"
           of type "bool", parameter "e_value" of Double, parameter
           "bitscore" of Double, parameter "overlap_perc" of Double,
           parameter "maxaccepts" of Double, parameter "heatmap" of type
           "bool", parameter "low_val" of type "bool", parameter "vertical"
           of type "bool", parameter "show_blanks" of type "bool"
        :returns: instance of type "HMMER_Output" (HMMER Output) ->
           structure: parameter "report_name" of type "data_obj_name",
           parameter "report_ref" of type "data_obj_ref"
        """
        return self._client.call_method('kb_hmmer.HMMER_EnvBioelement_Search',
                                        [params], self._service_ver, context)

    def status(self, context=None):
        return self._client.call_method('kb_hmmer.status',
                                        [], self._service_ver, context)
