Vim�UnDo� H�]%�-��+l^
���zTڧD��9�E'<��   �       �                           O9Cw    _�                     �       ����                                                                                                                                                                                                                                                                                                                                                             O5#z     �   �            5�_�                    �       ����                                                                                                                                                                                                                                                                                                                                                             O5#z     �   �               �   �                      5�_�                    �        ����                                                                                                                                                                                                                                                                                                                            �           �                   O5#�     �   �              +   +   ;+from base.datastore.properties import SerializableProperty   +   +   +class TestObj1(db.Model):   %+    payload = SerializableProperty()   +   +   +class TestObj2(object):   +   #+    def __init__(self, exception):   #+        self.exception = exception   +   +   /+class TestSaveLazyChildren(unittest.TestCase):   +   +    def test(self):   ,+        from google.appengine.ext import db   +   +        payload = TestObj1()    +        payload.payload = 'foo'   +   9+        dp = TestObj1(payload=TestObj2(payload.payload))   +        dp.put()   +   ++        #COMMENT THIS OUT FOR THIS TO PASS   +        dp = db.get(dp.key())   +   6+        self.assertEqual(dp.payload.exception, 'foo')5�_�                    �        ����                                                                                                                                                                                                                                                                                                                            �           �                   O5#�     �   �   �           5�_�                    �       ����                                                                                                                                                                                                                                                                                                                            �           �                   O5#�    �   �            5�_�                    �        ����                                                                                                                                                                                                                                                                                                                            �           �                   O5#�    �   �   �          *        #COMMENT THIS OUT FOR THIS TO PASS5�_�                    H        ����                                                                                                                                                                                                                                                                                                                            �           �                   O5��     �   G   I          1        self.assertEqual(token.orig_value, 'foo')5�_�      	              H        ����                                                                                                                                                                                                                                                                                                                            �           �                   O5��    �   H   J   �              �   H   J   �    5�_�      
           	   �        ����                                                                                                                                                                                                                                                                                                                            �           �                   O5�     �   �   �   �       �   �   �   �    5�_�   	              
   �       ����                                                                                                                                                                                                                                                                                                                            �           �                   O5�     �   �   �                  print 5�_�   
                 �        ����                                                                                                                                                                                                                                                                                                                            �           �                   O5�     �   �   �   �       �   �   �   �    5�_�                    �        ����                                                                                                                                                                                                                                                                                                                            �           �                   O5�    �   �   �   �              �   �   �   �    5�_�                            ����                                                                                                                                                                                                                                                                                                                            �           �                   O5��     �               �   """   """           from base import unittest       #from google.appengine.ext import db   ;from google.appengine.api import datastore as gae_datastore       *from base.datastore.properties import lazy               ,class SimpleLazyProperty(lazy.LazyProperty):       """       """           data_type = db.Text           2    def expand_value(self, value, model_instance):           return value       4    def contract_value(self, value, model_instance):           return value               class CPTEntity(db.Model):       """   4    Test entity used in the L{CopyFromTokenTestCase}       """           xml = SimpleLazyProperty()               /class CopyFromTokenTestCase(unittest.TestCase):       """   F    Test various scenarios where copy_from_token is called during lazy       operations.       """           )    def makeEntity(self, name, **kwargs):   J        # we can't put the CPTEntity directly in this test because we need   I        # to skip over the make_value_for_datastore stuff so we work with   )        # the lower level Entity instead.   =        e = gae_datastore.Entity(CPTEntity.kind(), name=name)               e.update(kwargs)               gae_datastore.Put([e])       H        # now we can get the entity from the datastore in the normal way   4        k = db.Key.from_path(CPTEntity.kind(), name)               return db.get(k)               def test_create(self):           """   P        A brand new entity that has not been persisted/loaded from the datastore   A        should have its changed/expanded values set appropriately           """            a = CPTEntity(xml='foo')               token = a.xml       4        self.assertIsInstance(token, lazy.LazyToken)       2        #self.assertEqual(token.orig_value, 'foo')   0        self.assertEqual(token.orig_value, None)   &        self.assertTrue(token.changed)   '        self.assertTrue(token.expanded)       2        self.assertEqual(token.raw_value(), 'foo')   5        self.assertEqual(token.cached_value(), 'foo')           '    def test_load_from_datastore(self):           """   ?        Test the token that has been loaded from the datastore.           """   -        a = self.makeEntity('bar', xml='foo')               token = a.xml       4        self.assertIsInstance(token, lazy.LazyToken)       1        self.assertEqual(token.orig_value, 'foo')       '        self.assertFalse(token.changed)   (        self.assertFalse(token.expanded)       2        self.assertEqual(token.raw_value(), 'foo')   5        self.assertEqual(token.cached_value(), 'foo')           %    def test_save_inited_value(self):           """   P        An entity loaded from the datastore and then immediately re-saved should   .        not cause contract value to be called.           """   6        a = self.makeEntity('bar', xml=db.Text('foo'))       !        def err(*args, **kwargs):   &            raise RuntimeError('boom')       8        self.patch(CPTEntity.xml, 'contract_value', err)               db.put(a)           7    def test_copy_token_from_saved_to_new_entity(self):           """   Q        Saving a new entity from a copied token from an already persisted entity.           """   -        a = self.makeEntity('bar', xml='foo')       %        b = CPTEntity(key_name='foo')               b.xml = a.xml       &        self.assertEqual(b.xml, 'foo')               db.put(b)       1        # reload the entity just to ensure sanity           c = db.get(b.key())       &        self.assertEqual(c.xml, 'foo')           7    def test_copy_token_from_new_to_saved_entity(self):           """   P        Saving an already existing entity from a copied token from a new entity.           """   1        a = CPTEntity(key_name='spam', xml='foo')   .        b = self.makeEntity('eggs', xml='bar')       &        self.assertEqual(a.xml, 'foo')   &        self.assertEqual(b.xml, 'bar')               b.xml = a.xml       &        self.assertEqual(b.xml, 'foo')               db.put(b)       1        # reload the entity just to ensure sanity           c = db.get(b.key())       &        self.assertEqual(c.xml, 'foo')           A    def test_copy_token_from_saved_to_already_saved_entity(self):           """   O        Saving an existing entity from a copied token from an already persisted           entity.           """   -        a = self.makeEntity('bar', xml='foo')   /        b = self.makeEntity('spam', xml='eggs')               b.xml = a.xml       &        self.assertEqual(b.xml, 'foo')               db.put(b)       1        # reload the entity just to ensure sanity           c = db.get(b.key())       &        self.assertEqual(c.xml, 'foo')           "    def test_set_after_copy(self):           """   K        Setting a new value after copying a token should persist correctly.           """   -        a = self.makeEntity('bar', xml='foo')   /        b = self.makeEntity('spam', xml='eggs')       '        self.assertEqual(b.xml, 'eggs')               b.xml = a.xml       &        self.assertEqual(b.xml, 'foo')               b.xml = 'hello world'       .        self.assertEqual(b.xml, 'hello world')               b.put()       1        # reload the entity just to ensure sanity           c = db.get(b.key())       .        self.assertEqual(c.xml, 'hello world')           &    def test_get_from_datastore(self):           """   N        This is the fundamental test for SKY-19102. Took 5 days to track down,   $        modify with extreme caution.           """   $        from documents import models       5        c = {'SectionBundles': {}, 'SupportData': {}}       3        draft_session = models.DraftSession(data=c)               draft_session.put()   3        draft_session = db.get(draft_session.key())       /        self.assertEqual(draft_session.data, c)           :from base.datastore.properties import SerializableProperty           class TestObj1(db.Model):   $    payload = SerializableProperty()           class TestObj2(object):       "    def __init__(self, exception):   "        self.exception = exception           .class TestSaveLazyChildren(unittest.TestCase):           def test(self):   +        from google.appengine.ext import db               payload = TestObj1()           payload.payload = 'foo'       8        dp = TestObj1(payload=TestObj2(payload.payload))           print 'save'           dp.put()               print 'get'           dp = db.get(dp.key())               print 'assert'   5        self.assertEqual(dp.payload.exception, 'foo')    5�_�                    �       ����                                                                                                                                                                                                                                                                                                                            �           �                   O5�     �   �   �                  print 'save'5�_�                    �       ����                                                                                                                                                                                                                                                                                                                            �           �                   O5�     �   �   �                  print 'get'5�_�                    �       ����                                                                                                                                                                                                                                                                                                                            �           �                   O5�    �   �   �                  print 'assert'5�_�                    H       ����                                                                                                                                                                                                                                                                                                                                                             O9?�    �   G   H          2        #self.assertEqual(token.orig_value, 'foo')5�_�                    �        ����                                                                                                                                                                                                                                                                                                                                                             O9Ca     �   �   �   �    5�_�                    �        ����                                                                                                                                                                                                                                                                                                                                                             O9Cb     �   �   �   �       5�_�                    �       ����                                                                                                                                                                                                                                                                                                                                                             O9Cj     �   �   �                  5�_�                    �        ����                                                                                                                                                                                                                                                                                                                                                             O9Ck     �   �   �   �       �   �   �   �    5�_�                     �       ����                                                                                                                                                                                                                                                                                                                                                             O9Cv    �   �   �                  dp = db.get(dp.key())5��