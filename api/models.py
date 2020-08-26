from django.db import models

class Country(models.Model):
    # unique=True,error_messages={'duplicates':'no duplicate country is allowed'}
    cname = models.CharField(max_length=50,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,blank=True,null=True)

    class Meta:
        ordering = ["cname"]

    def __str__(self):
        return self.cname

    def save(self, *args, **kwargs):
        self.cname = self.cname.upper()
        return super(Country, self).save(*args, **kwargs)


class Venue(models.Model):
    venue_name = models.CharField(max_length=100,blank=True,null=True)
    country = models.ForeignKey(Country,on_delete=models.SET_NULL,null=True)    
    created_at = models.DateTimeField(auto_now=True,blank=True,null=True)
    updated_at = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    
    class Meta:
        ordering = ["country"]

    def __str__(self):
        return f'{self.venue_name} {self.country}'

    def save(self, *args, **kwargs):
        self.venue_name = self.venue_name.upper() 
        return super(Venue, self).save(*args, **kwargs)



class Team(models.Model):
    team_name = models.CharField(max_length=100,blank=True,null=True)
    country = models.ForeignKey(Country, models.SET_NULL,null=True)
    created_at = models.DateTimeField(auto_now=True,blank=True,null=True)
    updated_at = models.DateTimeField(auto_now_add=True,blank=True,null=True)

    def __str__(self):
        return self.team_name

    def save(self, *args, **kwargs):
        self.team_name = self.team_name.upper()
        return super(Team, self).save(*args, **kwargs)

class Player(models.Model): 
    gender = (
        ('male','male'),
        ('female','female'),
        ('others','others')
    )   
    player_name = models.CharField(max_length=100,null=True,blank=True,help_text='Enter The name of player')
    age = models.IntegerField(null=True,blank=True)
    pic = models.ImageField(null=True,blank=True)
    gender = models.CharField(max_length=6,choices =gender ,null=True,blank=True)
    country = models.ForeignKey(Country,on_delete=models.SET_NULL,null=True)
    team = models.ForeignKey(Team,on_delete=models.SET_NULL,null=True)
    playerscore = models.IntegerField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now=True,blank=True,null=True)
    updated_at = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    

    def __str__(self):
        return self.player_name

    def __unicode__(self):
        return self.player_name   


    def save(self, *args, **kwargs):
        self.player_name = self.player_name.upper()
        return super(Player, self).save(*args, **kwargs)

class Match(models.Model):
    matchType = (
        ('test match','TEST MATCH'),
        ('one day international','ONE DAY INTERNATIONAL'),
        ('twenty 20 world cup','TWENTY 20 WORLD CUP')
    )
    date = models.DateTimeField(null=True,blank=True)
    match_no = models.IntegerField(blank=True,null=True)
    match_type = models.CharField(max_length=40,choices=matchType,null=True,blank=True)
    start_time = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    end_time = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    team1 = models.ForeignKey(Team,related_name='team1',on_delete=models.SET_NULL,null=True)
    team2 = models.ForeignKey(Team,related_name='team2',on_delete=models.SET_NULL,null=True)    
    venue = models.ForeignKey(Venue,max_length=100,related_name='venue',on_delete=models.SET_NULL,blank=True,null=True)
    winner = models.ForeignKey(Team,max_length=100,related_name='winner',on_delete=models.SET_NULL,blank=True,null=True)
    looser = models.ForeignKey(Team,max_length=100,related_name='looser',on_delete=models.SET_NULL,blank=True,null=True)
    man_of_the_match = models.ForeignKey(Player,max_length=100,related_name='man_of_the_match',on_delete=models.SET_NULL,blank=True,null=True)
    bowler_of_the_match =models.ForeignKey(Player,max_length=100,related_name='bowler_of_the_match',on_delete=models.SET_NULL,blank=True,null=True)
    best_fielder = models.ForeignKey(Player,max_length=100,related_name='best_fielder',on_delete=models.SET_NULL,blank=True,null=True)
    created_at = models.DateTimeField(auto_now=True,blank=True,null=True)
    updated_at = models.DateTimeField(auto_now_add=True,blank=True,null=True)
			
    def __str__(self):
        return f'{self.team1 } vs {self.team2} on { self.date }'

    class Meta:
        ordering = ["date"]
    # def save(self, *args, **kwargs):
    #     self.match_type = self.match_type.upper()        
    #     return super(Match, self).save(*args, **kwargs)

class Matchscorecard(models.Model):    
    match = models.OneToOneField(Match,on_delete=models.SET_NULL,blank=True,null=True)
    venue = models.ForeignKey(Venue,on_delete=models.SET_NULL,blank=True,null=True)
    wide =  models.IntegerField(null=True,blank=True)
    bounce =  models.IntegerField(null=True,blank=True)
    four =  models.IntegerField(null=True,blank=True)
    six = models.IntegerField(null=True,blank=True)

    def __str__(self):
        return f'{self.match} at {self.venue} on { self.match.date }'
