from django.db import models
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://tuismopqmafzhj:02dc15e1f6c6a03c8016276976f69fd1b234ab5a3c977b5d2ec3f57c23b23df6@ec2-54-83-49-109.compute-1.amazonaws.com:5432/deipbatmggnae8'
class maplist(models.Model):	
	mapName = models.CharField(max_length=60, null=False)	
	mapDesc = models.TextField(null=False)	
	mapLat = models.CharField(max_length=20, null=False)
	mapLng =  models.CharField(max_length=20, null=False)	
	mapTel = models.CharField(max_length=20, null=False)
	mapAddr = models.CharField(max_length=60, null=False)

	def __str__(self):		
		return self.mapName	
