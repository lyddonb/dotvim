Vim�UnDo� ���[��3�:��"�J5(sy#'���gj%���F   �                                  O���    _�                     �       ����                                                                                                                                                                                                                                                                                                                                                             O���     �   �   �   �              �   �   �   �    5�_�                    �   ,    ����                                                                                                                                                                                                                                                                                                                                                             O���     �   �   �   �      ,        from documents.api.elements import h5�_�                    �   K    ����                                                                                                                                                                                                                                                                                                                                                             O���     �   �   �   �              �   �   �   �    5�_�                    �   *    ����                                                                                                                                                                                                                                                                                                                                                             O���     �   �   �   �      ;        save_element_change_sets_for_fjit(fjit_change_sets)5�_�                    �   -    ����                                                                                                                                                                                                                                                                                                                                                             O���     �   �   �          .        from documents.draftsystem import save   H        return save.saveFjitChangeSets(fjit_change_sets, req.membership)5�_�                    �        ����                                                                                                                                                                                                                                                                                                                                                             O���     �   �   �   �              �   �   �   �    5�_�                    �   B    ����                                                                                                                                                                                                                                                                                                                                                             O��     �   �   �   �              �   �   �   �    5�_�      	              �   -    ����                                                                                                                                                                                                                                                                                                                                                             O��     �   �   �          .        from documents.draftsystem import save   N        return save.saveElementChangeSets(element_change_sets, req.membership)5�_�      
           	   �       ����                                                                                                                                                                                                                                                                                                                                                             O��     �   �   �   �      K        save_element_change_sets_for_fjit(req.membership, fjit_change_sets)5�_�   	              
   �   1    ����                                                                                                                                                                                                                                                                                                                                                             O��     �   �   �   �      R        return save_element_change_sets_for_fjit(req.membership, fjit_change_sets)5�_�   
                 y   
    ����                                                                                                                                                                                                                                                                                                                                                             O��O     �   y   {   �              �   y   {   �    5�_�                    z   B    ����                                                                                                                                                                                                                                                                                                                                                             O��_     �   z   }   �              �   z   |   �    5�_�                    }   -    ����                                                                                                                                                                                                                                                                                                                                                             O��q    �   |   }          .        from documents.draftsystem import save   `        return save.saveElementChangeSets(element_change_sets, req.membership, import_mode=True)5�_�                    �        ����                                                                                                                                                                                                                                                                                                                            �           �           v        O���     �   �   �   �   	        @decorators.account_required   =    def removeElementChangeSets(self, req, element_keynames):   7        """ <asargs>elementChangeSetList:Array</asargs>           <c></c>           """   .        from documents.draftsystem import save   M        return save.removeElementChangeSets(element_keynames, req.membership)        5�_�                     �        ����                                                                                                                                                                                                                                                                                                                            �           �           v        O���    �   �   �           5��