from django.test import TestCase
from . models import Topic, Document, Folder
from .serializers import DocumentSerializer


# Create your tests here.
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
    response = self.client.get('/documents/', {'folder': folder.id, 'topic': topic.id})

    # check response
    self.assertEqual(response.status_code, 200)
    self.assertEqual(len(response.data), 2)
    self.assertEqual(response.data[0]['name'], 'Document 1')
    self.assertEqual(response.data[1]['name'], 'Document 2')


# test models

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


def test_document_serializer(self):
    folder = Folder.objects.create(name='Test Folder')
    topic = Topic.objects.create(short_desc='Test Topic', long_desc='Long description')
    document = Document.objects.create(name='Test Document', folder=folder)
    document.topics.add(topic)
    serializer = DocumentSerializer(document)
    self.assertEqual(serializer.data['name'], 'Test Document')
    self.assertEqual(serializer.data['folder'], folder.id)
    self.assertEqual(serializer.data['topics'][0]['short_desc'], 'Test Topic')

# test views


def test_document_list_create_api_view(self):
    folder = Folder.objects.create(name='Test Folder')
    topic = Topic.objects.create(short_desc='Test Topic', long_desc='Long description')
    data = {'name': 'Test Document', 'folder': folder.id, 'topics': [topic.id]}
    response = self.client.post('/documents/', data=data, format='json')
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




