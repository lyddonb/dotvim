Vim�UnDo� #P��J�b���H�h� xt��*�N��}�                  self.fail(                             O5�    _�                             ����                                                                                                                                                                                                                                                                                                                                                             O5�I     �                        try:5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             O5�L     �                 �                 �                �            self.fail('expected AddOwnerRelationshipWizard.process_step to handle missing values in the request : ' + traceback.format_exc())5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             O5�M     �                        except:5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             O5�O    �               5            wiz = owners.AddOwnerRelationshipWizard()   9            wiz.process_step(request,context,0,None,None)5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             O5�]    �               5        wiz.process_step(request,context,0,None,None)5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             O5��     �                  """   Tests for L{section16.views}   """   import traceback   from base import unittest   "from section16.views import owners   from mock import Mock           8class TestAddOwnerRelationshipWizard(unittest.TestCase):           ;    # test for https://jira.webfilings.com/browse/SKY-22295   :    # process_step is called before the form is validated.   A    def test_process_step_0_handles_missing_registrant_CIK(self):       *        context = {'account':'1234567890'}           request = Mock()   *        request.POST = {'registrant':None}               #try:   1        wiz = owners.AddOwnerRelationshipWizard()   ;        print wiz.process_step(request,context,0,None,None)           #except:   �            #self.fail('expected AddOwnerRelationshipWizard.process_step to handle missing values in the request : ' + traceback.format_exc())            5�_�                           ����                                                                                                                                                                                                                                                                                                                               �                 v       O5��     �               �            self.fail('expected AddOwnerRelationshipWizard.process_step to handle missing values in the request : ' + traceback.format_exc())5�_�      
                     ����                                                                                                                                                                                                                                                                                                                               �                 v       O5��     �               �            elf.fail('expected AddOwnerRelationshipWizard.process_step to handle missing values in the request : ' + traceback.format_exc())5�_�         	       
          ����                                                                                                                                                                                                                                                                                                                               �                 v       O5��     �               �            self.fail('expected AddOwnerRelationshipWizard.process_step to handle missing values in the request : ' + traceback.format_exc())5�_�   
                        ����                                                                                                                                                                                                                                                                                                                               �                 v       O5��     �               �                'expected AddOwnerRelationshipWizard.process_step to handle missing values in the request : ' + traceback.format_exc())5�_�                       o    ����                                                                                                                                                                                                                                                                                                                               �                 v       O5��     �               �                """expected AddOwnerRelationshipWizard.process_step to handle missing values in the request : ' + traceback.format_exc())5�_�                       N    ����                                                                                                                                                                                                                                                                                                                               �                 v       O5��     �               �                """expected AddOwnerRelationshipWizard.process_step to handle missing values in the request : """ + traceback.format_exc())5�_�                       0    ����                                                                                                                                                                                                                                                                                                                               �                 v       O5��     �               M                missing values in the request : """ + traceback.format_exc())5�_�                       7    ����                                                                                                                                                                                                                                                                                                                               �                 v       O5��    �               O                missing values in the request : %s""" + traceback.format_exc())5�_�                            ����                                                                                                                                                                                                                                                                                                                               N                 v       O5�    �                           self.fail(5�_�              
   	          ����                                                                                                                                                                                                                                                                                                                               �                 v       O5��     �                           self.fail(   �                'expected AddOwnerRelationshipWizard.process_step to handle missing values in the request : ' + traceback.format_exc())5��