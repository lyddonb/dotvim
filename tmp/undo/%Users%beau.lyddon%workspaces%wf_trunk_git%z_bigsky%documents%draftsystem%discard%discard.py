Vim�UnDo� ��U�*̕n�{�[S*�O�D2���%s�+����   �          I         0       0   0   0    Nֈg    _�                     �   1    ����                                                                                                                                                                                                                                                                                                                                                             N՘�     �   �              6    logging.error("The discard failed", exc_info=args)5�_�                    �   1    ����                                                                                                                                                                                                                                                                                                                                                             N՘�    �   �   �          2    logging.error("The discard failed", exc_info=)5�_�                    :   1    ����                                                                                                                                                                                                                                                                                                                                                             N՚�     �   9   ;   �      3def discard_all(membership_key, draft_session_key):5�_�                    C       ����                                                                                                                                                                                                                                                                                                                                                             N՛     �   B   C          >    membership = auth_utils.get_membership(key=membership_key)5�_�                    C       ����                                                                                                                                                                                                                                                                                                                                                             N՛     �   B   C          -    user_name = membership.get_display_name()5�_�                    B        ����                                                                                                                                                                                                                                                                                                                                                             N՛     �   B   D   �       �   B   D   �    5�_�                    C   &    ����                                                                                                                                                                                                                                                                                                                                                             N՛    �   B   D   �      '    user_name = kwargs.get('user_name')5�_�      	              �   D    ����                                                                                                                                                                                                                                                                                                                                                             N՝%     �   �   �   �      F                    discard_docdraft, discard_dsd, active, user_name):5�_�      
           	   �   N    ����                                                                                                                                                                                                                                                                                                                                                             N՝,     �   �   �   �      O                    discard_docdraft=discard_docdraft, discard_dsd=discard_dsd)5�_�   	              
   I   #    ����                                                                                                                                                                                                                                                                                                                                                             N՝<     �   H   J   �      $                    None, user_name)5�_�   
                 C       ����                                                                                                                                                                                                                                                                                                                                                             N՝J     �   B   D   �      +    user_name = kwargs.get('user_name', '')5�_�                    C       ����                                                                                                                                                                                                                                                                                                                                                             N՝J     �   B   D   �      (    user_name = kwargs.('user_name', '')5�_�                    B        ����                                                                                                                                                                                                                                                                                                                                                             N՝M     �   B   D   �       �   B   D   �    5�_�                    D       ����                                                                                                                                                                                                                                                                                                                                                             N՝U     �   C   E   �      +    user_name = kwargs.pop('user_name', '')5�_�                    B        ����                                                                                                                                                                                                                                                                                                                                                             N՝V     �   B   D   �       �   B   D   �    5�_�                    E   *    ����                                                                                                                                                                                                                                                                                                                                                             N՝\     �   D   F   �      /        user_name = kwargs.pop('user_name', '')5�_�                    E   *    ����                                                                                                                                                                                                                                                                                                                                                             N՝]     �   D   F   �      -        user_name = kwargs.pop('user_name''')5�_�                    E   *    ����                                                                                                                                                                                                                                                                                                                                                             N՝^    �   D   F   �      *        user_name = kwargs.pop('user_name'5�_�                    I   J    ����                                                                                                                                                                                                                                                                                                                                                             N՞M     �   H   J   �      K    dl.add_callable(_discard_other, draft_session_key, [], None, user_name)5�_�                    ~   L    ����                                                                                                                                                                                                                                                                                                                                                             N՞V     �   }      �      Ndef _discard_other(draft_session_key, sections_to_discard, active, user_name):5�_�                    �   8    ����                                                                                                                                                                                                                                                                                                                                                             N՞]    �   �   �   �      9    d.discard(draft_session, sections_to_discard, active)5�_�                    M   /    ����                                                                                                                                                                                                                                                                                                                                                             NՠI     �   L   N   �      0    dl.set_completion_callback(discard_callback)5�_�                    M   1    ����                                                                                                                                                                                                                                                                                                                                                             NՠI    �   L   N          2    dl.set_completion_callback(discard_callback, )5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             Nօ-     �               �   #from google.appengine.ext import db       $from auth import utils as auth_utils   3from base.deferred.response import DeferredResponse   3from base.deferred.deferredlist import DeferredList   (from documents import models as docmodel   )from documents.draftsystem import discard   2from documents.draftsystem.discard import elements   .from documents.draftsystem.discard import main       import logging               Fdef run(target_documentid, membership_obj, only_discard_sections_list,   C            discard_tree, discard_dsd, discard_docdraft, **kwargs):       """   O    Run discard for a document for the list of passed in sections. Also discard   M    the main draft items if their flags are set. This process will be handled       via the DeferredResponse.   '    @param target_documentid: C{String}   2    @param membership_obj: C{authmodel.Membership}   0    @param only_discard_sections_list: L{String}   #    @param discard_tree: C{Boolean}   "    @param discard_dsd: C{Boolean}   '    @param discard_docdraft: C{Boolean}       """       P    draft_session = discard.setup(target_documentid, only_discard_sections_list,   7                                  membership_obj.key())           if not draft_session:   7        return create_empty_response(target_documentid)       !    active = kwargs.get('active')       1    user_name = membership_obj.get_display_name()       :    deferred_response = DeferredResponse(serial_mode=True)       E    deferred_response.add_job(_discard_elements, draft_session.key(),   P                    membership_obj.key(), only_discard_sections_list, user_name)   B    deferred_response.add_job(_discard_other, draft_session.key(),   B                    only_discard_sections_list, active, user_name)   A    deferred_response.add_job(_discard_main, draft_session.key(),   O                    only_discard_sections_list, discard_tree, discard_docdraft,   3                    discard_dsd, active, user_name)       ?    deferred_response.set_completion_callback(discard_callback)   P    deferred_response.set_job_fail_callback(discard_failed, draft_session.key(),   >                                            active, user_name)       )    result = deferred_response.run_jobs()           return result           Ddef discard_all(membership_key, draft_session_key, *args, **kwargs):       """   Q    Discard all drafts for a draft session. Creates the deferred list for discard       and returns it be ran.   $    @param membership_key: C{db.Key}   '    @param draft_session_key: C{db.Key}       """   '    dl = DeferredList(serial_mode=True)           user_name = ''       if 'user_name' in kwargs:   +        user_name = kwargs.pop('user_name')       M    dl.add_callable(_discard_elements, draft_session_key, membership_key, [],                       user_name)   U    dl.add_callable(_discard_other, draft_session_key, [], None, user_name, **kwargs)   K    dl.add_callable(_discard_main, draft_session_key, [], True, True, True,   .                    None, user_name, **kwargs)       4    dl.set_completion_callback(discard_callback, [])   L    dl.set_job_errorback(discard_failed, draft_session_key, None, user_name)           return dl           &def create_empty_response(documentid):       """   B    Create an empty discard result object and set the document id.        @param documentid: C{String}       """   %    result = docmodel.DiscardResult()   "    result.documentid = documentid       result.keynamesRemoved = []        result.keynamesModified = []        result.sectionsModified = []       return result           def discard_callback(values):       """   L    This will return a deferred entity that will run or continue the discard       process.   ,    @param values: L{docmodel.DiscardResult}       """       if values:           return values[-1]       return None           Mdef _discard_elements(draft_session_key, membership_key, sections_to_discard,   !                      user_name):       """   M    Run the element discard process. This will apply the change set rules and   L    remove or update the change sets either directly or indirectly linked to   !    the sections being discarded.   '    @param draft_session_key: C{db.Key}   $    @param membership_key: C{db.Key}   )    @param sections_to_discard: L{String}       @param user_name: C{String}       """   :    logging.info("Discarding Elements for %s" % user_name)       0    #TODO: build in batching the element discard   -    draft_session = db.get(draft_session_key)   6    discard_change_sets = elements.DiscardChangeSets()   S    discard_change_sets.discard(draft_session, membership_key, sections_to_discard)           Xdef _discard_other(draft_session_key, sections_to_discard, active, user_name, **kwargs):       """   N    Discard the support data that is not directly on the draft session for the   L    document being discarded. This is support data linked via element links.   '    @param draft_session_key: C{db.Key}   )    @param sections_to_discard: L{String}   #    @param active: C{collab.Active}       @param user_name: C{String}       """   D    logging.info("Discarding Other Support Data for %s" % user_name)   Q    #the main discard process is complete. we now need to cleanup the other draft   /    #sessions that maybe linked to this discard   -    draft_session = db.get(draft_session_key)       '    d = main.OtherDraftSessionDiscard()   C    d.discard(draft_session, sections_to_discard, active, **kwargs)       >    logging.info('Done with other draft session support data')           Ndef _discard_main(draft_session_key, only_discard_sections_list, discard_tree,   P                    discard_docdraft, discard_dsd, active, user_name, **kwargs):       """   O    Run the main discard. This will discard the core linked drafts on the draft   G    session along with the sections and directly attached support data.   '    @param draft_session_key: C{db.Key}   0    @param only_discard_sections_list: L{String}   #    @param discard_tree: C{Boolean}   '    @param discard_docdraft: C{Boolean}   "    @param discard_dsd: C{Boolean}   #    @param active: C{collab.Active}       @param user_name: C{String}       """   =    logging.info("Discarding Main Drafts for %s" % user_name)       -    draft_session = db.get(draft_session_key)            discard = main.MainDiscard()   >    discard.discard(draft_session, only_discard_sections_list,   =                    active=active, discard_tree=discard_tree,   Y                    discard_docdraft=discard_docdraft, discard_dsd=discard_dsd, **kwargs)   *    logging.info("Done with main discard")   #    discard.cleanup_draft_session()   ;    logging.info("Finished with discard and notifications")       return discard.complete()           Sdef discard_failed(failure, draft_session_key, active, user_name, *args, **kwargs):       """   O    When the discard fails we need to log as much information as possible. Also   7    cleans up the draft session and updates the status.   ,    @param failure: C{base.deferred.Failure}   '    @param draft_session_key: C{db.Key}   #    @param active: C{collab.Active}       @param user_name: C{String}       """   8    logging.info("Discarding Failed for %s" % user_name)           fail_message = ''       if failure.value:   )        fail_message = str(failure.value)   D    logging.error("Error in discard of type %s with a message of %s"   H        % (str(failure.type), fail_message), exc_info=failure.traceback)       D    logging.error("The discard failed", exc_info=failure.get_info())5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             Nօs     �      !   �       �         �    5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             Nօv     �      !          def _run5�_�                             ����                                                                                                                                                                                                                                                                                                                                                             Nօ�     �                 
def _run()5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             Nօ�     �                 5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             Nօ�     �                 5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             Nօ�     �                 5�_�                             ����                                                                                                                                                                                                                                                                                                                                                             Nօ�    �                 5�_�      !               D       ����                                                                                                                                                                                                                                                                                                                                                             NևZ     �   D   F   �    5�_�       "           !   E       ����                                                                                                                                                                                                                                                                                                                                                             Nև[     �   E   G          :    sections_to_discard = discard.add_all_sections_if_none�   D   G   �              5�_�   !   #           "   E        ����                                                                                                                                                                                                                                                                                                                                                             Nևw     �   E   G   �       �   E   G   �    5�_�   "   $           #   G   ;    ����                                                                                                                                                                                                                                                                                                                                                             Nև�     �   F   H   �      <    sections_to_discard = discard.add_all_sections_if_none()5�_�   #   %           $   I   M    ����                                                                                                                                                                                                                                                                                                                                                             Nև�     �   H   K   �      M    dl.add_callable(_discard_elements, draft_session_key, membership_key, [],5�_�   $   &           %   J       ����                                                                                                                                                                                                                                                                                                                                                             Nև�     �   I   K   �              sections_to_discard5�_�   %   '           &   J       ����                                                                                                                                                                                                                                                                                                                                                             Nև�     �   I   K   �                  sections_to_discard5�_�   &   (           '   J       ����                                                                                                                                                                                                                                                                                                                                                             Nև�     �   I   K   �      #                sections_to_discard5�_�   '   )           (   K       ����                                                                                                                                                                                                                                                                                                                                                             Nև�     �   I   K   �      '                    sections_to_discard   
user_name)�   J   L   �                          user_name)5�_�   (   *           )   K   7    ����                                                                                                                                                                                                                                                                                                                                                             Nև�     �   J   L   �      U    dl.add_callable(_discard_other, draft_session_key, [], None, user_name, **kwargs)5�_�   )   +           *   K   7    ����                                                                                                                                                                                                                                                                                                                                                             Nև�     �   J   M   �      Q    dl.add_callable(_discard_other, draft_session_key, None, user_name, **kwargs)5�_�   *   ,           +   M   6    ����                                                                                                                                                                                                                                                                                                                                                             Nև�     �   L   N   �      K    dl.add_callable(_discard_main, draft_session_key, [], True, True, True,5�_�   +   -           ,   M   6    ����                                                                                                                                                                                                                                                                                                                                                             Nև�     �   L   O   �      G    dl.add_callable(_discard_main, draft_session_key, True, True, True,5�_�   ,   .           -   O       ����                                                                                                                                                                                                                                                                                                                                                             Nև�    �   M   O   �      %                    True, True, True,   None, user_name, **kwargs)�   N   P   �      .                    None, user_name, **kwargs)5�_�   -   /           .   G   %    ����                                                                                                                                                                                                                                                                                                                                                             NֈT     �   G   I   �    5�_�   .   0           /   H       ����                                                                                                                                                                                                                                                                                                                                                             NֈU     �   G   I   �          5�_�   /               0   H   ;    ����                                                                                                                                                                                                                                                                                                                                                             Nֈf    �   H   J   �          �   H   J   �    5��