Vim�UnDo� 5_#���c#mȵ�l���㤢�D3+Ƀ|~��   3                                  OSe    _�                        
    ����                                                                                                                                                                                                                                                                                                                                                             OR�     �         /    5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             OR�    �         0          5�_�                       !    ����                                                                                                                                                                                                                                                                                                                                                             OR�&     �                !    firstName = db.StringProperty5�_�                       !    ����                                                                                                                                                                                                                                                                                                                                                             OR�'     �         1          �         0    5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             OR�0    �         1      "    lastName = db.StringProeprty()5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             OR��     �               1   #from google.appengine.ext import db       from nomo import datastore               class User(db.Model):       """       """       +    name = db.StringProperty(indexed=False)   /    username = db.StringProperty(indexed=False)   #    firstName = db.StringProperty()   "    lastName = db.StringProperty()       7    dateJoined = db.DateTimeProperty(auto_now_add=True)           @classmethod       def build_key(cls, id_):   0        return db.Key.from_path(cls.kind(), id_)               class Credentials(db.Model):       """            @parent: The L{User} object.       @key_name: C{type:id}   K    @ivar type: The type identity for the user, e.g. twitter, facebook etc.       """           type = db.StringProperty()       id = db.StringProperty()       ,    token = db.StringProperty(indexed=False)   -    secret = db.StringProperty(indexed=False)               @property       def user(self):           return self.parent()               !class ProviderResponse(db.Model):       """       """       #    data = datastore.JsonProperty()5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             OR��     �         1    5�_�      	                      ����                                                                                                                                                                                                                                                                                                                                                             OR��    �         2       5�_�      
           	           ����                                                                                                                                                                                                                                                                                                                                                             OR�     �         3    5�_�   	              
           ����                                                                                                                                                                                                                                                                                                                                                             OR�     �         4       5�_�   
                        ����                                                                                                                                                                                                                                                                                                                                                             OR�
     �         4      =pyamf.register_class(TreeDraft, 'documents.models.TreeDraft')5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             OR�     �         4      8pyamf.register_class(User, 'documents.models.TreeDraft')5�_�                      (    ����                                                                                                                                                                                                                                                                                                                                                             OR�    �         4      3pyamf.register_class(User, 'user.models.TreeDraft')5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             OR�    �                 5�_�                    3   "    ����                                                                                                                                                                                                                                                                                                                                                             OSN     �   3                  �   3            5�_�                     4        ����                                                                                                                                                                                                                                                                                                                                                             OSd    �   2              #    data = datastore.JsonProperty()    5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             OR�     �         4      w5��