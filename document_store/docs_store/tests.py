from django.test import TestCase
from rest_framework.test import APITestCase, RequestsClient

from .models import Topic, Document, Folder
from .serializers import DocumentSerializer, TopicSerializer, FolderSerializer
import base64


class ListFoldersTestCase(APITestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.client = RequestsClient()

    def setUp(self):
        Folder.objects.all().delete()

    def test_folder_list(self):
        response = self.client.get('/folders/')
        print(response.status_code)
        self.assertEqual(response.status_code, 200)


class ListDocumentsTestCase(APITestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.client = RequestsClient()

    def setUp(self):
        Document.objects.all().delete()

    def test_document_list(self):
        response = self.client.get('/documents/')
        print(response.status_code)
        self.assertEqual(response.status_code, 200)


class ListTopicsTestCase(APITestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.client = RequestsClient()

    def setUp(self):
        Topic.objects.all().delete()

    def test_folder_list(self):
        #response = self.client.get('http://127.0.0.1:8010/topics/')
        response = self.client.get('/topics/')
        print(response.status_code)
        self.assertEqual(response.status_code, 200)


class GetDocumentsWithTopicInFolderTestCase(APITestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.client = RequestsClient()

    def setUp(self):
        Topic.objects.all().delete()
        Folder.objects.all().delete()
        Document.objects.all().delete()

    def test_get_documents_with_topic_in_folder(self):
        # create test data
        folder = Folder.objects.create(name='CustomerFeedback')
        topic = Topic.objects.create(short_desc='SpekiLove!', long_desc='Long description')
        document1 = Document.objects.create(name='Document 1', folder=folder)
        document1.topics.add(topic)
        document2 = Document.objects.create(name='Document 2', folder=folder)
        document2.topics.add(topic)
        document3 = Document.objects.create(name='Document 3', folder=folder)
        document3.topics.add(Topic.objects.create(short_desc='Other Topic', long_desc='Other Long description'))

        # make API request


        response = self.client.get('/documents/', {'folder': 'CustomerFeedback!', 'topic': 'SpekiLove!'})

        # check response

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0]['topics'][0]['short_desc'], 'SpekiLove!')
        self.assertEqual(response.data[1]['topics'][0]['short_desc'], 'SpekiLove!')
        self.assertEqual(response.data[2]['topics'][0]['short_desc'], 'Other Topic')
        self.assertEqual(response.data[0]['name'], 'Document 1')
        self.assertEqual(response.data[1]['name'], 'Document 2')

# test models


class StrTestCase(APITestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.client = RequestsClient()

    def setUp(self):
        Topic.objects.all().delete()
        Document.objects.all().delete()
        Folder.objects.all().delete()

    def test_topic_str(self):
        topic = Topic.objects.create(short_desc='Test Topic', long_desc='Long description')
        self.assertEqual(str(topic), 'Test Topic')

    def test_folder_str(self):
        folder = Folder.objects.create(name='Test Folder')
        self.assertEqual(str(folder), 'Test Folder')

    def test_document_str(self):
        folder = Folder.objects.create(name='Test Folder')
        document = Document.objects.create(name='Test Document', folder=folder)
        self.assertEqual(str(document), 'Test Document')


# test serializers

class SerializersTestCase(APITestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.client = RequestsClient()

    def setUp(self):
        Topic.objects.all().delete()
        Document.objects.all().delete()
        Folder.objects.all().delete()

    def test_document_serializer(self):
        folder = Folder.objects.create(name='Test Folder')
        topic = Topic.objects.create(short_desc='Test Topic', long_desc='Long description')
        document = Document.objects.create(name='Test Document', folder=folder)
        document.topics.add(topic)
        serializer = DocumentSerializer(document)
        self.assertEqual(serializer.data['name'], 'Test Document')
        self.assertEqual(serializer.data['folder'], folder.id)
        self.assertEqual(serializer.data['topics'][0]['short_desc'], 'Test Topic')


# Test views

class ApiCreateUpdateDeleteTestCase(APITestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.client = RequestsClient()

    def setUp(self):
        Topic.objects.all().delete()
        Document.objects.all().delete()
        Folder.objects.all().delete()

    def test_document_list_create_api_view(self):
        folder = Folder.objects.create(name='Test Folder')
        topic = Topic.objects.create(short_desc='Test Topic', long_desc='Long description')
        document = Document.objects.create(name='Test Document', folder=folder)
        document.topics.add(topic)
        data = {'name': 'Test Document', 'folder': folder.id}
        fh = open('Das_rules_applied.xlsx', 'rb')
        data['file'] = str(base64.b64encode(fh.read()))
        response = self.client.post('/documents/', data=data, format='json')
        print(response.data)
        self.assertEqual(response.status_code, 201)

    def test_document_retrieve_update_destroy_api_view(self):
        folder = Folder.objects.create(name='Test Folder')
        topic = Topic.objects.create(short_desc='Test Topic', long_desc='Long description')
        document = Document.objects.create(name='Test Document', folder=folder)
        document.topics.add(topic)
        response = self.client.get('/documents/{}/'.format(document.id))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['name'], 'Test Document')
        data = {'name': 'Test Document Updated', 'folder': folder.id, 'topics': [topic.id]}
        response = self.client.put('/documents/{}/'.format(document.id), data=data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['name'], 'Test Document Updated')
        response = self.client.delete('/documents/{}/'.format(document.id))
        self.assertEqual(response.status_code, 204)
















