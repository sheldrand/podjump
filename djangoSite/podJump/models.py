# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines for those models you wish to give write DB access
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals

from django.db import models

class Agtagenttypes(models.Model):
    agenttypeid = models.IntegerField(db_column='agentTypeID', primary_key=True) # Field name made lowercase.
    agenttype = models.CharField(db_column='agentType', max_length=50, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'agtAgentTypes'

class Agtagents(models.Model):
    agentid = models.IntegerField(db_column='agentID', primary_key=True) # Field name made lowercase.
    divisionid = models.IntegerField(db_column='divisionID', blank=True, null=True) # Field name made lowercase.
    corporationid = models.IntegerField(db_column='corporationID', blank=True, null=True) # Field name made lowercase.
    locationid = models.IntegerField(db_column='locationID', blank=True, null=True) # Field name made lowercase.
    level = models.IntegerField(blank=True, null=True)
    quality = models.IntegerField(blank=True, null=True)
    agenttypeid = models.IntegerField(db_column='agentTypeID', blank=True, null=True) # Field name made lowercase.
    islocator = models.IntegerField(db_column='isLocator', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'agtAgents'

class Agtresearchagents(models.Model):
    agentid = models.IntegerField(db_column='agentID', primary_key=True) # Field name made lowercase.
    typeid = models.IntegerField(db_column='typeID') # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'agtResearchAgents'

class Certcerts(models.Model):
    certid = models.IntegerField(db_column='certID', primary_key=True) # Field name made lowercase.
    description = models.TextField(blank=True)
    groupid = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True)
    class Meta:
        managed = False
        db_table = 'certCerts'

class Certmasteries(models.Model):
    typeid = models.IntegerField(db_column='typeID', blank=True, null=True) # Field name made lowercase.
    masterylevel = models.IntegerField(db_column='masteryLevel', blank=True, null=True) # Field name made lowercase.
    certid = models.IntegerField(db_column='certID', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'certMasteries'

class Certskills(models.Model):
    certid = models.IntegerField(db_column='certID', blank=True, null=True) # Field name made lowercase.
    skillid = models.IntegerField(db_column='skillID', blank=True, null=True) # Field name made lowercase.
    certlevelint = models.IntegerField(db_column='certLevelInt', blank=True, null=True) # Field name made lowercase.
    skilllevel = models.IntegerField(db_column='skillLevel', blank=True, null=True) # Field name made lowercase.
    certleveltext = models.CharField(db_column='certLevelText', max_length=8, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'certSkills'

class Chrancestries(models.Model):
    ancestryid = models.IntegerField(db_column='ancestryID', primary_key=True) # Field name made lowercase.
    ancestryname = models.CharField(db_column='ancestryName', max_length=200, blank=True) # Field name made lowercase.
    bloodlineid = models.IntegerField(db_column='bloodlineID', blank=True, null=True) # Field name made lowercase.
    description = models.CharField(max_length=2000, blank=True)
    perception = models.IntegerField(blank=True, null=True)
    willpower = models.IntegerField(blank=True, null=True)
    charisma = models.IntegerField(blank=True, null=True)
    memory = models.IntegerField(blank=True, null=True)
    intelligence = models.IntegerField(blank=True, null=True)
    iconid = models.IntegerField(db_column='iconID', blank=True, null=True) # Field name made lowercase.
    shortdescription = models.CharField(db_column='shortDescription', max_length=1000, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'chrAncestries'

class Chrattributes(models.Model):
    attributeid = models.IntegerField(db_column='attributeID', primary_key=True) # Field name made lowercase.
    attributename = models.CharField(db_column='attributeName', max_length=100, blank=True) # Field name made lowercase.
    description = models.CharField(max_length=1000, blank=True)
    iconid = models.IntegerField(db_column='iconID', blank=True, null=True) # Field name made lowercase.
    shortdescription = models.CharField(db_column='shortDescription', max_length=1000, blank=True) # Field name made lowercase.
    notes = models.CharField(max_length=1000, blank=True)
    class Meta:
        managed = False
        db_table = 'chrAttributes'

class Chrbloodlines(models.Model):
    bloodlineid = models.IntegerField(db_column='bloodlineID', primary_key=True) # Field name made lowercase.
    bloodlinename = models.CharField(db_column='bloodlineName', max_length=200, blank=True) # Field name made lowercase.
    raceid = models.IntegerField(db_column='raceID', blank=True, null=True) # Field name made lowercase.
    description = models.CharField(max_length=2000, blank=True)
    maledescription = models.CharField(db_column='maleDescription', max_length=2000, blank=True) # Field name made lowercase.
    femaledescription = models.CharField(db_column='femaleDescription', max_length=2000, blank=True) # Field name made lowercase.
    shiptypeid = models.IntegerField(db_column='shipTypeID', blank=True, null=True) # Field name made lowercase.
    corporationid = models.IntegerField(db_column='corporationID', blank=True, null=True) # Field name made lowercase.
    perception = models.IntegerField(blank=True, null=True)
    willpower = models.IntegerField(blank=True, null=True)
    charisma = models.IntegerField(blank=True, null=True)
    memory = models.IntegerField(blank=True, null=True)
    intelligence = models.IntegerField(blank=True, null=True)
    iconid = models.IntegerField(db_column='iconID', blank=True, null=True) # Field name made lowercase.
    shortdescription = models.CharField(db_column='shortDescription', max_length=1000, blank=True) # Field name made lowercase.
    shortmaledescription = models.CharField(db_column='shortMaleDescription', max_length=1000, blank=True) # Field name made lowercase.
    shortfemaledescription = models.CharField(db_column='shortFemaleDescription', max_length=1000, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'chrBloodlines'

class Chrfactions(models.Model):
    factionid = models.IntegerField(db_column='factionID', primary_key=True) # Field name made lowercase.
    factionname = models.CharField(db_column='factionName', max_length=100, blank=True) # Field name made lowercase.
    description = models.CharField(max_length=1000, blank=True)
    raceids = models.IntegerField(db_column='raceIDs', blank=True, null=True) # Field name made lowercase.
    solarsystemid = models.IntegerField(db_column='solarSystemID', blank=True, null=True) # Field name made lowercase.
    corporationid = models.IntegerField(db_column='corporationID', blank=True, null=True) # Field name made lowercase.
    sizefactor = models.TextField(db_column='sizeFactor', blank=True) # Field name made lowercase. This field type is a guess.
    stationcount = models.IntegerField(db_column='stationCount', blank=True, null=True) # Field name made lowercase.
    stationsystemcount = models.IntegerField(db_column='stationSystemCount', blank=True, null=True) # Field name made lowercase.
    militiacorporationid = models.IntegerField(db_column='militiaCorporationID', blank=True, null=True) # Field name made lowercase.
    iconid = models.IntegerField(db_column='iconID', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'chrFactions'

class Chrraces(models.Model):
    raceid = models.IntegerField(db_column='raceID', primary_key=True) # Field name made lowercase.
    racename = models.CharField(db_column='raceName', max_length=100, blank=True) # Field name made lowercase.
    description = models.CharField(max_length=1000, blank=True)
    iconid = models.IntegerField(db_column='iconID', blank=True, null=True) # Field name made lowercase.
    shortdescription = models.CharField(db_column='shortDescription', max_length=500, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'chrRaces'

class Crpactivities(models.Model):
    activityid = models.IntegerField(db_column='activityID', primary_key=True) # Field name made lowercase.
    activityname = models.CharField(db_column='activityName', max_length=200, blank=True) # Field name made lowercase.
    description = models.CharField(max_length=2000, blank=True)
    class Meta:
        managed = False
        db_table = 'crpActivities'

class Crpnpccorporationdivisions(models.Model):
    corporationid = models.IntegerField(db_column='corporationID', primary_key=True) # Field name made lowercase.
    divisionid = models.IntegerField(db_column='divisionID', primary_key=True) # Field name made lowercase.
    size = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'crpNPCCorporationDivisions'

class Crpnpccorporationresearchfields(models.Model):
    skillid = models.IntegerField(db_column='skillID', primary_key=True) # Field name made lowercase.
    corporationid = models.IntegerField(db_column='corporationID', primary_key=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'crpNPCCorporationResearchFields'

class Crpnpccorporationtrades(models.Model):
    corporationid = models.IntegerField(db_column='corporationID', primary_key=True) # Field name made lowercase.
    typeid = models.IntegerField(db_column='typeID', primary_key=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'crpNPCCorporationTrades'

class Crpnpccorporations(models.Model):
    corporationid = models.IntegerField(db_column='corporationID', primary_key=True) # Field name made lowercase.
    size = models.CharField(max_length=1, blank=True)
    extent = models.CharField(max_length=1, blank=True)
    solarsystemid = models.IntegerField(db_column='solarSystemID', blank=True, null=True) # Field name made lowercase.
    investorid1 = models.IntegerField(db_column='investorID1', blank=True, null=True) # Field name made lowercase.
    investorshares1 = models.IntegerField(db_column='investorShares1', blank=True, null=True) # Field name made lowercase.
    investorid2 = models.IntegerField(db_column='investorID2', blank=True, null=True) # Field name made lowercase.
    investorshares2 = models.IntegerField(db_column='investorShares2', blank=True, null=True) # Field name made lowercase.
    investorid3 = models.IntegerField(db_column='investorID3', blank=True, null=True) # Field name made lowercase.
    investorshares3 = models.IntegerField(db_column='investorShares3', blank=True, null=True) # Field name made lowercase.
    investorid4 = models.IntegerField(db_column='investorID4', blank=True, null=True) # Field name made lowercase.
    investorshares4 = models.IntegerField(db_column='investorShares4', blank=True, null=True) # Field name made lowercase.
    friendid = models.IntegerField(db_column='friendID', blank=True, null=True) # Field name made lowercase.
    enemyid = models.IntegerField(db_column='enemyID', blank=True, null=True) # Field name made lowercase.
    publicshares = models.IntegerField(db_column='publicShares', blank=True, null=True) # Field name made lowercase.
    initialprice = models.IntegerField(db_column='initialPrice', blank=True, null=True) # Field name made lowercase.
    minsecurity = models.TextField(db_column='minSecurity', blank=True) # Field name made lowercase. This field type is a guess.
    scattered = models.IntegerField(blank=True, null=True)
    fringe = models.IntegerField(blank=True, null=True)
    corridor = models.IntegerField(blank=True, null=True)
    hub = models.IntegerField(blank=True, null=True)
    border = models.IntegerField(blank=True, null=True)
    factionid = models.IntegerField(db_column='factionID', blank=True, null=True) # Field name made lowercase.
    sizefactor = models.TextField(db_column='sizeFactor', blank=True) # Field name made lowercase. This field type is a guess.
    stationcount = models.IntegerField(db_column='stationCount', blank=True, null=True) # Field name made lowercase.
    stationsystemcount = models.IntegerField(db_column='stationSystemCount', blank=True, null=True) # Field name made lowercase.
    description = models.CharField(max_length=8000, blank=True)
    iconid = models.IntegerField(db_column='iconID', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'crpNPCCorporations'

class Crpnpcdivisions(models.Model):
    divisionid = models.IntegerField(db_column='divisionID', primary_key=True) # Field name made lowercase.
    divisionname = models.CharField(db_column='divisionName', max_length=200, blank=True) # Field name made lowercase.
    description = models.CharField(max_length=2000, blank=True)
    leadertype = models.CharField(db_column='leaderType', max_length=200, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'crpNPCDivisions'

class Crtcategories(models.Model):
    categoryid = models.IntegerField(db_column='categoryID', primary_key=True) # Field name made lowercase.
    description = models.CharField(max_length=1000, blank=True)
    categoryname = models.CharField(db_column='categoryName', max_length=512, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'crtCategories'

class Crtcertificates(models.Model):
    certificateid = models.IntegerField(db_column='certificateID', primary_key=True) # Field name made lowercase.
    categoryid = models.IntegerField(db_column='categoryID', blank=True, null=True) # Field name made lowercase.
    classid = models.IntegerField(db_column='classID', blank=True, null=True) # Field name made lowercase.
    grade = models.IntegerField(blank=True, null=True)
    corpid = models.IntegerField(db_column='corpID', blank=True, null=True) # Field name made lowercase.
    iconid = models.IntegerField(db_column='iconID', blank=True, null=True) # Field name made lowercase.
    description = models.CharField(max_length=1000, blank=True)
    class Meta:
        managed = False
        db_table = 'crtCertificates'

class Crtclasses(models.Model):
    classid = models.IntegerField(db_column='classID', primary_key=True) # Field name made lowercase.
    description = models.CharField(max_length=1000, blank=True)
    classname = models.CharField(db_column='className', max_length=512, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'crtClasses'

class Crtrecommendations(models.Model):
    recommendationid = models.IntegerField(db_column='recommendationID', primary_key=True) # Field name made lowercase.
    shiptypeid = models.IntegerField(db_column='shipTypeID', blank=True, null=True) # Field name made lowercase.
    certificateid = models.IntegerField(db_column='certificateID', blank=True, null=True) # Field name made lowercase.
    recommendationlevel = models.IntegerField(db_column='recommendationLevel') # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'crtRecommendations'

class Crtrelationships(models.Model):
    relationshipid = models.IntegerField(db_column='relationshipID', primary_key=True) # Field name made lowercase.
    parentid = models.IntegerField(db_column='parentID', blank=True, null=True) # Field name made lowercase.
    parenttypeid = models.IntegerField(db_column='parentTypeID', blank=True, null=True) # Field name made lowercase.
    parentlevel = models.IntegerField(db_column='parentLevel', blank=True, null=True) # Field name made lowercase.
    childid = models.IntegerField(db_column='childID', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'crtRelationships'

class Dgmattributecategories(models.Model):
    categoryid = models.IntegerField(db_column='categoryID', primary_key=True) # Field name made lowercase.
    categoryname = models.CharField(db_column='categoryName', max_length=100, blank=True) # Field name made lowercase.
    categorydescription = models.CharField(db_column='categoryDescription', max_length=400, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'dgmAttributeCategories'

class Dgmattributetypes(models.Model):
    attributeid = models.IntegerField(db_column='attributeID', primary_key=True) # Field name made lowercase.
    attributename = models.CharField(db_column='attributeName', max_length=100, blank=True) # Field name made lowercase.
    description = models.CharField(max_length=1000, blank=True)
    iconid = models.IntegerField(db_column='iconID', blank=True, null=True) # Field name made lowercase.
    defaultvalue = models.TextField(db_column='defaultValue', blank=True) # Field name made lowercase. This field type is a guess.
    published = models.IntegerField(blank=True, null=True)
    displayname = models.CharField(db_column='displayName', max_length=100, blank=True) # Field name made lowercase.
    unitid = models.IntegerField(db_column='unitID', blank=True, null=True) # Field name made lowercase.
    stackable = models.IntegerField(blank=True, null=True)
    highisgood = models.IntegerField(db_column='highIsGood', blank=True, null=True) # Field name made lowercase.
    categoryid = models.IntegerField(db_column='categoryID', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'dgmAttributeTypes'

class Dgmeffects(models.Model):
    effectid = models.IntegerField(db_column='effectID', primary_key=True) # Field name made lowercase.
    effectname = models.CharField(db_column='effectName', max_length=400, blank=True) # Field name made lowercase.
    effectcategory = models.IntegerField(db_column='effectCategory', blank=True, null=True) # Field name made lowercase.
    preexpression = models.IntegerField(db_column='preExpression', blank=True, null=True) # Field name made lowercase.
    postexpression = models.IntegerField(db_column='postExpression', blank=True, null=True) # Field name made lowercase.
    description = models.CharField(max_length=1000, blank=True)
    guid = models.CharField(max_length=60, blank=True)
    iconid = models.IntegerField(db_column='iconID', blank=True, null=True) # Field name made lowercase.
    isoffensive = models.IntegerField(db_column='isOffensive', blank=True, null=True) # Field name made lowercase.
    isassistance = models.IntegerField(db_column='isAssistance', blank=True, null=True) # Field name made lowercase.
    durationattributeid = models.IntegerField(db_column='durationAttributeID', blank=True, null=True) # Field name made lowercase.
    trackingspeedattributeid = models.IntegerField(db_column='trackingSpeedAttributeID', blank=True, null=True) # Field name made lowercase.
    dischargeattributeid = models.IntegerField(db_column='dischargeAttributeID', blank=True, null=True) # Field name made lowercase.
    rangeattributeid = models.IntegerField(db_column='rangeAttributeID', blank=True, null=True) # Field name made lowercase.
    falloffattributeid = models.IntegerField(db_column='falloffAttributeID', blank=True, null=True) # Field name made lowercase.
    disallowautorepeat = models.IntegerField(db_column='disallowAutoRepeat', blank=True, null=True) # Field name made lowercase.
    published = models.IntegerField(blank=True, null=True)
    displayname = models.CharField(db_column='displayName', max_length=100, blank=True) # Field name made lowercase.
    iswarpsafe = models.IntegerField(db_column='isWarpSafe', blank=True, null=True) # Field name made lowercase.
    rangechance = models.IntegerField(db_column='rangeChance', blank=True, null=True) # Field name made lowercase.
    electronicchance = models.IntegerField(db_column='electronicChance', blank=True, null=True) # Field name made lowercase.
    propulsionchance = models.IntegerField(db_column='propulsionChance', blank=True, null=True) # Field name made lowercase.
    distribution = models.IntegerField(blank=True, null=True)
    sfxname = models.CharField(db_column='sfxName', max_length=20, blank=True) # Field name made lowercase.
    npcusagechanceattributeid = models.IntegerField(db_column='npcUsageChanceAttributeID', blank=True, null=True) # Field name made lowercase.
    npcactivationchanceattributeid = models.IntegerField(db_column='npcActivationChanceAttributeID', blank=True, null=True) # Field name made lowercase.
    fittingusagechanceattributeid = models.IntegerField(db_column='fittingUsageChanceAttributeID', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'dgmEffects'

class Dgmtypeattributes(models.Model):
    typeid = models.IntegerField(db_column='typeID', primary_key=True) # Field name made lowercase.
    attributeid = models.IntegerField(db_column='attributeID', primary_key=True) # Field name made lowercase.
    valueint = models.IntegerField(db_column='valueInt', blank=True, null=True) # Field name made lowercase.
    valuefloat = models.TextField(db_column='valueFloat', blank=True) # Field name made lowercase. This field type is a guess.
    class Meta:
        managed = False
        db_table = 'dgmTypeAttributes'

class Dgmtypeeffects(models.Model):
    typeid = models.IntegerField(db_column='typeID', primary_key=True) # Field name made lowercase.
    effectid = models.IntegerField(db_column='effectID', primary_key=True) # Field name made lowercase.
    isdefault = models.IntegerField(db_column='isDefault', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'dgmTypeEffects'

class Eveicons(models.Model):
    iconid = models.IntegerField(db_column='iconID', primary_key=True) # Field name made lowercase.
    iconfile = models.CharField(db_column='iconFile', max_length=500) # Field name made lowercase.
    description = models.TextField()
    class Meta:
        managed = False
        db_table = 'eveIcons'

class Eveunits(models.Model):
    unitid = models.IntegerField(db_column='unitID', primary_key=True) # Field name made lowercase.
    unitname = models.CharField(db_column='unitName', max_length=100, blank=True) # Field name made lowercase.
    displayname = models.CharField(db_column='displayName', max_length=50, blank=True) # Field name made lowercase.
    description = models.CharField(max_length=1000, blank=True)
    class Meta:
        managed = False
        db_table = 'eveUnits'

class Invblueprinttypes(models.Model):
    blueprinttypeid = models.IntegerField(db_column='blueprintTypeID', primary_key=True) # Field name made lowercase.
    parentblueprinttypeid = models.IntegerField(db_column='parentBlueprintTypeID', blank=True, null=True) # Field name made lowercase.
    producttypeid = models.IntegerField(db_column='productTypeID', blank=True, null=True) # Field name made lowercase.
    productiontime = models.IntegerField(db_column='productionTime', blank=True, null=True) # Field name made lowercase.
    techlevel = models.IntegerField(db_column='techLevel', blank=True, null=True) # Field name made lowercase.
    researchproductivitytime = models.IntegerField(db_column='researchProductivityTime', blank=True, null=True) # Field name made lowercase.
    researchmaterialtime = models.IntegerField(db_column='researchMaterialTime', blank=True, null=True) # Field name made lowercase.
    researchcopytime = models.IntegerField(db_column='researchCopyTime', blank=True, null=True) # Field name made lowercase.
    researchtechtime = models.IntegerField(db_column='researchTechTime', blank=True, null=True) # Field name made lowercase.
    productivitymodifier = models.IntegerField(db_column='productivityModifier', blank=True, null=True) # Field name made lowercase.
    materialmodifier = models.IntegerField(db_column='materialModifier', blank=True, null=True) # Field name made lowercase.
    wastefactor = models.IntegerField(db_column='wasteFactor', blank=True, null=True) # Field name made lowercase.
    maxproductionlimit = models.IntegerField(db_column='maxProductionLimit', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'invBlueprintTypes'

class Invcategories(models.Model):
    categoryid = models.IntegerField(db_column='categoryID', primary_key=True) # Field name made lowercase.
    categoryname = models.CharField(db_column='categoryName', max_length=200, blank=True) # Field name made lowercase.
    description = models.CharField(max_length=6000, blank=True)
    iconid = models.IntegerField(db_column='iconID', blank=True, null=True) # Field name made lowercase.
    published = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'invCategories'

class Invcontrabandtypes(models.Model):
    factionid = models.IntegerField(db_column='factionID', primary_key=True) # Field name made lowercase.
    typeid = models.IntegerField(db_column='typeID') # Field name made lowercase.
    standingloss = models.TextField(db_column='standingLoss', blank=True) # Field name made lowercase. This field type is a guess.
    confiscateminsec = models.TextField(db_column='confiscateMinSec', blank=True) # Field name made lowercase. This field type is a guess.
    finebyvalue = models.TextField(db_column='fineByValue', blank=True) # Field name made lowercase. This field type is a guess.
    attackminsec = models.TextField(db_column='attackMinSec', blank=True) # Field name made lowercase. This field type is a guess.
    class Meta:
        managed = False
        db_table = 'invContrabandTypes'

class Invcontroltowerresourcepurposes(models.Model):
    purpose = models.IntegerField(primary_key=True)
    purposetext = models.CharField(db_column='purposeText', max_length=100, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'invControlTowerResourcePurposes'

class Invcontroltowerresources(models.Model):
    controltowertypeid = models.IntegerField(db_column='controlTowerTypeID', primary_key=True) # Field name made lowercase.
    resourcetypeid = models.IntegerField(db_column='resourceTypeID', primary_key=True) # Field name made lowercase.
    purpose = models.IntegerField(blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    minsecuritylevel = models.TextField(db_column='minSecurityLevel', blank=True) # Field name made lowercase. This field type is a guess.
    factionid = models.IntegerField(db_column='factionID', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'invControlTowerResources'

class Invflags(models.Model):
    flagid = models.IntegerField(db_column='flagID', primary_key=True) # Field name made lowercase.
    flagname = models.CharField(db_column='flagName', max_length=200, blank=True) # Field name made lowercase.
    flagtext = models.CharField(db_column='flagText', max_length=100, blank=True) # Field name made lowercase.
    orderid = models.IntegerField(db_column='orderID', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'invFlags'

class Invgroups(models.Model):
    groupid = models.IntegerField(db_column='groupID', primary_key=True) # Field name made lowercase.
    categoryid = models.IntegerField(db_column='categoryID', blank=True, null=True) # Field name made lowercase.
    groupname = models.CharField(db_column='groupName', max_length=200, blank=True) # Field name made lowercase.
    description = models.CharField(max_length=6000, blank=True)
    iconid = models.IntegerField(db_column='iconID', blank=True, null=True) # Field name made lowercase.
    usebaseprice = models.IntegerField(db_column='useBasePrice', blank=True, null=True) # Field name made lowercase.
    allowmanufacture = models.IntegerField(db_column='allowManufacture', blank=True, null=True) # Field name made lowercase.
    allowrecycler = models.IntegerField(db_column='allowRecycler', blank=True, null=True) # Field name made lowercase.
    anchored = models.IntegerField(blank=True, null=True)
    anchorable = models.IntegerField(blank=True, null=True)
    fittablenonsingleton = models.IntegerField(db_column='fittableNonSingleton', blank=True, null=True) # Field name made lowercase.
    published = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'invGroups'

class Invitems(models.Model):
    itemid = models.IntegerField(db_column='itemID', primary_key=True) # Field name made lowercase.
    typeid = models.IntegerField(db_column='typeID') # Field name made lowercase.
    ownerid = models.IntegerField(db_column='ownerID') # Field name made lowercase.
    locationid = models.IntegerField(db_column='locationID') # Field name made lowercase.
    flagid = models.IntegerField(db_column='flagID') # Field name made lowercase.
    quantity = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'invItems'

class Invmarketgroups(models.Model):
    marketgroupid = models.IntegerField(db_column='marketGroupID', primary_key=True) # Field name made lowercase.
    parentgroupid = models.IntegerField(db_column='parentGroupID', blank=True, null=True) # Field name made lowercase.
    marketgroupname = models.CharField(db_column='marketGroupName', max_length=200, blank=True) # Field name made lowercase.
    description = models.CharField(max_length=6000, blank=True)
    iconid = models.IntegerField(db_column='iconID', blank=True, null=True) # Field name made lowercase.
    hastypes = models.IntegerField(db_column='hasTypes', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'invMarketGroups'

class Invmetagroups(models.Model):
    metagroupid = models.IntegerField(db_column='metaGroupID', primary_key=True) # Field name made lowercase.
    metagroupname = models.CharField(db_column='metaGroupName', max_length=200, blank=True) # Field name made lowercase.
    description = models.CharField(max_length=2000, blank=True)
    iconid = models.IntegerField(db_column='iconID', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'invMetaGroups'

class Invmetatypes(models.Model):
    typeid = models.IntegerField(db_column='typeID', primary_key=True) # Field name made lowercase.
    parenttypeid = models.IntegerField(db_column='parentTypeID', blank=True, null=True) # Field name made lowercase.
    metagroupid = models.IntegerField(db_column='metaGroupID', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'invMetaTypes'

class Invnames(models.Model):
    itemid = models.IntegerField(db_column='itemID', primary_key=True) # Field name made lowercase.
    itemname = models.CharField(db_column='itemName', max_length=400) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'invNames'

class Invpositions(models.Model):
    itemid = models.IntegerField(db_column='itemID', primary_key=True) # Field name made lowercase.
    x = models.TextField() # This field type is a guess.
    y = models.TextField() # This field type is a guess.
    z = models.TextField() # This field type is a guess.
    yaw = models.TextField(blank=True) # This field type is a guess.
    pitch = models.TextField(blank=True) # This field type is a guess.
    roll = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        managed = False
        db_table = 'invPositions'

class Invtypematerials(models.Model):
    typeid = models.IntegerField(db_column='typeID', primary_key=True) # Field name made lowercase.
    materialtypeid = models.IntegerField(db_column='materialTypeID', primary_key=True) # Field name made lowercase.
    quantity = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'invTypeMaterials'

class Invtypereactions(models.Model):
    reactiontypeid = models.IntegerField(db_column='reactionTypeID', primary_key=True) # Field name made lowercase.
    input = models.IntegerField(primary_key=True)
    typeid = models.IntegerField(db_column='typeID', primary_key=True) # Field name made lowercase.
    quantity = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'invTypeReactions'

class Invtypes(models.Model):
    typeid = models.IntegerField(db_column='typeID', primary_key=True) # Field name made lowercase.
    groupid = models.IntegerField(db_column='groupID', blank=True, null=True) # Field name made lowercase.
    typename = models.CharField(db_column='typeName', max_length=200, blank=True) # Field name made lowercase.
    description = models.CharField(max_length=6000, blank=True)
    mass = models.TextField(blank=True) # This field type is a guess.
    volume = models.TextField(blank=True) # This field type is a guess.
    capacity = models.TextField(blank=True) # This field type is a guess.
    portionsize = models.IntegerField(db_column='portionSize', blank=True, null=True) # Field name made lowercase.
    raceid = models.IntegerField(db_column='raceID', blank=True, null=True) # Field name made lowercase.
    baseprice = models.TextField(db_column='basePrice', blank=True) # Field name made lowercase. This field type is a guess.
    published = models.IntegerField(blank=True, null=True)
    marketgroupid = models.IntegerField(db_column='marketGroupID', blank=True, null=True) # Field name made lowercase.
    chanceofduplicating = models.TextField(db_column='chanceOfDuplicating', blank=True) # Field name made lowercase. This field type is a guess.
    class Meta:
        managed = False
        db_table = 'invTypes'

class Invuniquenames(models.Model):
    itemid = models.IntegerField(db_column='itemID', primary_key=True) # Field name made lowercase.
    itemname = models.CharField(db_column='itemName', max_length=400) # Field name made lowercase.
    groupid = models.IntegerField(db_column='groupID', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'invUniqueNames'

class Mapcelestialstatistics(models.Model):
    celestialid = models.IntegerField(db_column='celestialID', primary_key=True) # Field name made lowercase.
    temperature = models.TextField(blank=True) # This field type is a guess.
    spectralclass = models.CharField(db_column='spectralClass', max_length=10, blank=True) # Field name made lowercase.
    luminosity = models.TextField(blank=True) # This field type is a guess.
    age = models.TextField(blank=True) # This field type is a guess.
    life = models.TextField(blank=True) # This field type is a guess.
    orbitradius = models.TextField(db_column='orbitRadius', blank=True) # Field name made lowercase. This field type is a guess.
    eccentricity = models.TextField(blank=True) # This field type is a guess.
    massdust = models.TextField(db_column='massDust', blank=True) # Field name made lowercase. This field type is a guess.
    massgas = models.TextField(db_column='massGas', blank=True) # Field name made lowercase. This field type is a guess.
    fragmented = models.IntegerField(blank=True, null=True)
    density = models.TextField(blank=True) # This field type is a guess.
    surfacegravity = models.TextField(db_column='surfaceGravity', blank=True) # Field name made lowercase. This field type is a guess.
    escapevelocity = models.TextField(db_column='escapeVelocity', blank=True) # Field name made lowercase. This field type is a guess.
    orbitperiod = models.TextField(db_column='orbitPeriod', blank=True) # Field name made lowercase. This field type is a guess.
    rotationrate = models.TextField(db_column='rotationRate', blank=True) # Field name made lowercase. This field type is a guess.
    locked = models.IntegerField(blank=True, null=True)
    pressure = models.TextField(blank=True) # This field type is a guess.
    radius = models.TextField(blank=True) # This field type is a guess.
    mass = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        managed = False
        db_table = 'mapCelestialStatistics'

class Mapconstellationjumps(models.Model):
    fromregionid = models.IntegerField(db_column='fromRegionID', blank=True, null=True) # Field name made lowercase.
    fromconstellationid = models.IntegerField(db_column='fromConstellationID', primary_key=True) # Field name made lowercase.
    toconstellationid = models.IntegerField(db_column='toConstellationID', primary_key=True) # Field name made lowercase.
    toregionid = models.IntegerField(db_column='toRegionID', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'mapConstellationJumps'

class Mapconstellations(models.Model):
    regionid = models.IntegerField(db_column='regionID', blank=True, null=True) # Field name made lowercase.
    constellationid = models.IntegerField(db_column='constellationID', primary_key=True) # Field name made lowercase.
    constellationname = models.CharField(db_column='constellationName', max_length=200, blank=True) # Field name made lowercase.
    x = models.TextField(blank=True) # This field type is a guess.
    y = models.TextField(blank=True) # This field type is a guess.
    z = models.TextField(blank=True) # This field type is a guess.
    xmin = models.TextField(db_column='xMin', blank=True) # Field name made lowercase. This field type is a guess.
    xmax = models.TextField(db_column='xMax', blank=True) # Field name made lowercase. This field type is a guess.
    ymin = models.TextField(db_column='yMin', blank=True) # Field name made lowercase. This field type is a guess.
    ymax = models.TextField(db_column='yMax', blank=True) # Field name made lowercase. This field type is a guess.
    zmin = models.TextField(db_column='zMin', blank=True) # Field name made lowercase. This field type is a guess.
    zmax = models.TextField(db_column='zMax', blank=True) # Field name made lowercase. This field type is a guess.
    factionid = models.IntegerField(db_column='factionID', blank=True, null=True) # Field name made lowercase.
    radius = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        managed = False
        db_table = 'mapConstellations'

class Mapdenormalize(models.Model):
    itemid = models.IntegerField(db_column='itemID', primary_key=True) # Field name made lowercase.
    typeid = models.IntegerField(db_column='typeID', blank=True, null=True) # Field name made lowercase.
    groupid = models.IntegerField(db_column='groupID', blank=True, null=True) # Field name made lowercase.
    solarsystemid = models.IntegerField(db_column='solarSystemID', blank=True, null=True) # Field name made lowercase.
    constellationid = models.IntegerField(db_column='constellationID', blank=True, null=True) # Field name made lowercase.
    regionid = models.IntegerField(db_column='regionID', blank=True, null=True) # Field name made lowercase.
    orbitid = models.IntegerField(db_column='orbitID', blank=True, null=True) # Field name made lowercase.
    x = models.TextField(blank=True) # This field type is a guess.
    y = models.TextField(blank=True) # This field type is a guess.
    z = models.TextField(blank=True) # This field type is a guess.
    radius = models.TextField(blank=True) # This field type is a guess.
    itemname = models.CharField(db_column='itemName', max_length=200, blank=True) # Field name made lowercase.
    security = models.TextField(blank=True) # This field type is a guess.
    celestialindex = models.IntegerField(db_column='celestialIndex', blank=True, null=True) # Field name made lowercase.
    orbitindex = models.IntegerField(db_column='orbitIndex', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'mapDenormalize'

class Mapjumps(models.Model):
    stargateid = models.IntegerField(db_column='stargateID', primary_key=True) # Field name made lowercase.
    celestialid = models.IntegerField(db_column='celestialID', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'mapJumps'

class Maplandmarks(models.Model):
    landmarkid = models.IntegerField(db_column='landmarkID', primary_key=True) # Field name made lowercase.
    landmarkname = models.CharField(db_column='landmarkName', max_length=100, blank=True) # Field name made lowercase.
    description = models.CharField(max_length=7000, blank=True)
    locationid = models.IntegerField(db_column='locationID', blank=True, null=True) # Field name made lowercase.
    x = models.TextField(blank=True) # This field type is a guess.
    y = models.TextField(blank=True) # This field type is a guess.
    z = models.TextField(blank=True) # This field type is a guess.
    radius = models.TextField(blank=True) # This field type is a guess.
    iconid = models.IntegerField(db_column='iconID', blank=True, null=True) # Field name made lowercase.
    importance = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'mapLandmarks'

class Maplocationscenes(models.Model):
    locationid = models.IntegerField(db_column='locationID', primary_key=True) # Field name made lowercase.
    graphicid = models.IntegerField(db_column='graphicID', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'mapLocationScenes'

class Maplocationwormholeclasses(models.Model):
    locationid = models.IntegerField(db_column='locationID', primary_key=True) # Field name made lowercase.
    wormholeclassid = models.IntegerField(db_column='wormholeClassID', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'mapLocationWormholeClasses'

class Mapregionjumps(models.Model):
    fromregionid = models.IntegerField(db_column='fromRegionID', primary_key=True) # Field name made lowercase.
    toregionid = models.IntegerField(db_column='toRegionID', primary_key=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'mapRegionJumps'

class Mapregions(models.Model):
    regionid = models.IntegerField(db_column='regionID', primary_key=True) # Field name made lowercase.
    regionname = models.CharField(db_column='regionName', max_length=200, blank=True) # Field name made lowercase.
    x = models.TextField(blank=True) # This field type is a guess.
    y = models.TextField(blank=True) # This field type is a guess.
    z = models.TextField(blank=True) # This field type is a guess.
    xmin = models.TextField(db_column='xMin', blank=True) # Field name made lowercase. This field type is a guess.
    xmax = models.TextField(db_column='xMax', blank=True) # Field name made lowercase. This field type is a guess.
    ymin = models.TextField(db_column='yMin', blank=True) # Field name made lowercase. This field type is a guess.
    ymax = models.TextField(db_column='yMax', blank=True) # Field name made lowercase. This field type is a guess.
    zmin = models.TextField(db_column='zMin', blank=True) # Field name made lowercase. This field type is a guess.
    zmax = models.TextField(db_column='zMax', blank=True) # Field name made lowercase. This field type is a guess.
    factionid = models.IntegerField(db_column='factionID', blank=True, null=True) # Field name made lowercase.
    radius = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        managed = False
        db_table = 'mapRegions'

class Mapsolarsystemjumps(models.Model):
    fromregionid = models.IntegerField(db_column='fromRegionID', blank=True, null=True) # Field name made lowercase.
    fromconstellationid = models.IntegerField(db_column='fromConstellationID', blank=True, null=True) # Field name made lowercase.
    fromsolarsystemid = models.IntegerField(db_column='fromSolarSystemID', primary_key=True) # Field name made lowercase.
    tosolarsystemid = models.IntegerField(db_column='toSolarSystemID', primary_key=True) # Field name made lowercase.
    toconstellationid = models.IntegerField(db_column='toConstellationID', blank=True, null=True) # Field name made lowercase.
    toregionid = models.IntegerField(db_column='toRegionID', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'mapSolarSystemJumps'

class Mapsolarsystems(models.Model):
    regionid = models.IntegerField(db_column='regionID', blank=True, null=True) # Field name made lowercase.
    constellationid = models.IntegerField(db_column='constellationID', blank=True, null=True) # Field name made lowercase.
    solarsystemid = models.IntegerField(db_column='solarSystemID', primary_key=True) # Field name made lowercase.
    solarsystemname = models.CharField(db_column='solarSystemName', max_length=200, blank=True) # Field name made lowercase.
    x = models.TextField(blank=True) # This field type is a guess.
    y = models.TextField(blank=True) # This field type is a guess.
    z = models.TextField(blank=True) # This field type is a guess.
    xmin = models.TextField(db_column='xMin', blank=True) # Field name made lowercase. This field type is a guess.
    xmax = models.TextField(db_column='xMax', blank=True) # Field name made lowercase. This field type is a guess.
    ymin = models.TextField(db_column='yMin', blank=True) # Field name made lowercase. This field type is a guess.
    ymax = models.TextField(db_column='yMax', blank=True) # Field name made lowercase. This field type is a guess.
    zmin = models.TextField(db_column='zMin', blank=True) # Field name made lowercase. This field type is a guess.
    zmax = models.TextField(db_column='zMax', blank=True) # Field name made lowercase. This field type is a guess.
    luminosity = models.TextField(blank=True) # This field type is a guess.
    border = models.IntegerField(blank=True, null=True)
    fringe = models.IntegerField(blank=True, null=True)
    corridor = models.IntegerField(blank=True, null=True)
    hub = models.IntegerField(blank=True, null=True)
    international = models.IntegerField(blank=True, null=True)
    regional = models.IntegerField(blank=True, null=True)
    constellation = models.IntegerField(blank=True, null=True)
    security = models.TextField(blank=True) # This field type is a guess.
    factionid = models.IntegerField(db_column='factionID', blank=True, null=True) # Field name made lowercase.
    radius = models.TextField(blank=True) # This field type is a guess.
    suntypeid = models.IntegerField(db_column='sunTypeID', blank=True, null=True) # Field name made lowercase.
    securityclass = models.CharField(db_column='securityClass', max_length=2, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'mapSolarSystems'

class Mapuniverse(models.Model):
    universeid = models.IntegerField(db_column='universeID', primary_key=True) # Field name made lowercase.
    universename = models.CharField(db_column='universeName', max_length=100, blank=True) # Field name made lowercase.
    x = models.TextField(blank=True) # This field type is a guess.
    y = models.TextField(blank=True) # This field type is a guess.
    z = models.TextField(blank=True) # This field type is a guess.
    xmin = models.TextField(db_column='xMin', blank=True) # Field name made lowercase. This field type is a guess.
    xmax = models.TextField(db_column='xMax', blank=True) # Field name made lowercase. This field type is a guess.
    ymin = models.TextField(db_column='yMin', blank=True) # Field name made lowercase. This field type is a guess.
    ymax = models.TextField(db_column='yMax', blank=True) # Field name made lowercase. This field type is a guess.
    zmin = models.TextField(db_column='zMin', blank=True) # Field name made lowercase. This field type is a guess.
    zmax = models.TextField(db_column='zMax', blank=True) # Field name made lowercase. This field type is a guess.
    radius = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        managed = False
        db_table = 'mapUniverse'

class Planetschematics(models.Model):
    schematicid = models.IntegerField(db_column='schematicID', primary_key=True) # Field name made lowercase.
    schematicname = models.CharField(db_column='schematicName', max_length=510, blank=True) # Field name made lowercase.
    cycletime = models.IntegerField(db_column='cycleTime', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'planetSchematics'

class Planetschematicspinmap(models.Model):
    schematicid = models.IntegerField(db_column='schematicID', primary_key=True) # Field name made lowercase.
    pintypeid = models.IntegerField(db_column='pinTypeID', primary_key=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'planetSchematicsPinMap'

class Planetschematicstypemap(models.Model):
    schematicid = models.IntegerField(db_column='schematicID', primary_key=True) # Field name made lowercase.
    typeid = models.IntegerField(db_column='typeID', primary_key=True) # Field name made lowercase.
    quantity = models.IntegerField(blank=True, null=True)
    isinput = models.IntegerField(db_column='isInput', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'planetSchematicsTypeMap'

class Ramactivities(models.Model):
    activityid = models.IntegerField(db_column='activityID', primary_key=True) # Field name made lowercase.
    activityname = models.CharField(db_column='activityName', max_length=200, blank=True) # Field name made lowercase.
    iconno = models.CharField(db_column='iconNo', max_length=5, blank=True) # Field name made lowercase.
    description = models.CharField(max_length=2000, blank=True)
    published = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'ramActivities'

class Ramassemblylinestations(models.Model):
    stationid = models.IntegerField(db_column='stationID', primary_key=True) # Field name made lowercase.
    assemblylinetypeid = models.IntegerField(db_column='assemblyLineTypeID', primary_key=True) # Field name made lowercase.
    quantity = models.IntegerField(blank=True, null=True)
    stationtypeid = models.IntegerField(db_column='stationTypeID', blank=True, null=True) # Field name made lowercase.
    ownerid = models.IntegerField(db_column='ownerID', blank=True, null=True) # Field name made lowercase.
    solarsystemid = models.IntegerField(db_column='solarSystemID', blank=True, null=True) # Field name made lowercase.
    regionid = models.IntegerField(db_column='regionID', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'ramAssemblyLineStations'

class Ramassemblylinetypedetailpercategory(models.Model):
    assemblylinetypeid = models.IntegerField(db_column='assemblyLineTypeID', primary_key=True) # Field name made lowercase.
    categoryid = models.IntegerField(db_column='categoryID', primary_key=True) # Field name made lowercase.
    timemultiplier = models.TextField(db_column='timeMultiplier', blank=True) # Field name made lowercase. This field type is a guess.
    materialmultiplier = models.TextField(db_column='materialMultiplier', blank=True) # Field name made lowercase. This field type is a guess.
    class Meta:
        managed = False
        db_table = 'ramAssemblyLineTypeDetailPerCategory'

class Ramassemblylinetypedetailpergroup(models.Model):
    assemblylinetypeid = models.IntegerField(db_column='assemblyLineTypeID', primary_key=True) # Field name made lowercase.
    groupid = models.IntegerField(db_column='groupID', primary_key=True) # Field name made lowercase.
    timemultiplier = models.TextField(db_column='timeMultiplier', blank=True) # Field name made lowercase. This field type is a guess.
    materialmultiplier = models.TextField(db_column='materialMultiplier', blank=True) # Field name made lowercase. This field type is a guess.
    class Meta:
        managed = False
        db_table = 'ramAssemblyLineTypeDetailPerGroup'

class Ramassemblylinetypes(models.Model):
    assemblylinetypeid = models.IntegerField(db_column='assemblyLineTypeID', primary_key=True) # Field name made lowercase.
    assemblylinetypename = models.CharField(db_column='assemblyLineTypeName', max_length=200, blank=True) # Field name made lowercase.
    description = models.CharField(max_length=2000, blank=True)
    basetimemultiplier = models.TextField(db_column='baseTimeMultiplier', blank=True) # Field name made lowercase. This field type is a guess.
    basematerialmultiplier = models.TextField(db_column='baseMaterialMultiplier', blank=True) # Field name made lowercase. This field type is a guess.
    volume = models.TextField(blank=True) # This field type is a guess.
    activityid = models.IntegerField(db_column='activityID', blank=True, null=True) # Field name made lowercase.
    mincostperhour = models.TextField(db_column='minCostPerHour', blank=True) # Field name made lowercase. This field type is a guess.
    class Meta:
        managed = False
        db_table = 'ramAssemblyLineTypes'

class Ramassemblylines(models.Model):
    assemblylineid = models.IntegerField(db_column='assemblyLineID', primary_key=True) # Field name made lowercase.
    assemblylinetypeid = models.IntegerField(db_column='assemblyLineTypeID', blank=True, null=True) # Field name made lowercase.
    containerid = models.IntegerField(db_column='containerID', blank=True, null=True) # Field name made lowercase.
    nextfreetime = models.DateTimeField(db_column='nextFreeTime', blank=True, null=True) # Field name made lowercase.
    uigroupingid = models.IntegerField(db_column='UIGroupingID', blank=True, null=True) # Field name made lowercase.
    costinstall = models.TextField(db_column='costInstall', blank=True) # Field name made lowercase. This field type is a guess.
    costperhour = models.TextField(db_column='costPerHour', blank=True) # Field name made lowercase. This field type is a guess.
    restrictionmask = models.IntegerField(db_column='restrictionMask', blank=True, null=True) # Field name made lowercase.
    discountpergoodstandingpoint = models.TextField(db_column='discountPerGoodStandingPoint', blank=True) # Field name made lowercase. This field type is a guess.
    surchargeperbadstandingpoint = models.TextField(db_column='surchargePerBadStandingPoint', blank=True) # Field name made lowercase. This field type is a guess.
    minimumstanding = models.TextField(db_column='minimumStanding', blank=True) # Field name made lowercase. This field type is a guess.
    minimumcharsecurity = models.TextField(db_column='minimumCharSecurity', blank=True) # Field name made lowercase. This field type is a guess.
    minimumcorpsecurity = models.TextField(db_column='minimumCorpSecurity', blank=True) # Field name made lowercase. This field type is a guess.
    maximumcharsecurity = models.TextField(db_column='maximumCharSecurity', blank=True) # Field name made lowercase. This field type is a guess.
    maximumcorpsecurity = models.TextField(db_column='maximumCorpSecurity', blank=True) # Field name made lowercase. This field type is a guess.
    ownerid = models.IntegerField(db_column='ownerID', blank=True, null=True) # Field name made lowercase.
    activityid = models.IntegerField(db_column='activityID', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'ramAssemblyLines'

class Raminstallationtypecontents(models.Model):
    installationtypeid = models.IntegerField(db_column='installationTypeID', primary_key=True) # Field name made lowercase.
    assemblylinetypeid = models.IntegerField(db_column='assemblyLineTypeID', primary_key=True) # Field name made lowercase.
    quantity = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'ramInstallationTypeContents'

class Ramtyperequirements(models.Model):
    typeid = models.IntegerField(db_column='typeID', primary_key=True) # Field name made lowercase.
    activityid = models.IntegerField(db_column='activityID', primary_key=True) # Field name made lowercase.
    requiredtypeid = models.IntegerField(db_column='requiredTypeID', primary_key=True) # Field name made lowercase.
    quantity = models.IntegerField(blank=True, null=True)
    damageperjob = models.TextField(db_column='damagePerJob', blank=True) # Field name made lowercase. This field type is a guess.
    recycle = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'ramTypeRequirements'

class Staoperationservices(models.Model):
    operationid = models.IntegerField(db_column='operationID', primary_key=True) # Field name made lowercase.
    serviceid = models.IntegerField(db_column='serviceID', primary_key=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'staOperationServices'

class Staoperations(models.Model):
    activityid = models.IntegerField(db_column='activityID', blank=True, null=True) # Field name made lowercase.
    operationid = models.IntegerField(db_column='operationID', primary_key=True) # Field name made lowercase.
    operationname = models.CharField(db_column='operationName', max_length=200, blank=True) # Field name made lowercase.
    description = models.CharField(max_length=2000, blank=True)
    fringe = models.IntegerField(blank=True, null=True)
    corridor = models.IntegerField(blank=True, null=True)
    hub = models.IntegerField(blank=True, null=True)
    border = models.IntegerField(blank=True, null=True)
    ratio = models.IntegerField(blank=True, null=True)
    caldaristationtypeid = models.IntegerField(db_column='caldariStationTypeID', blank=True, null=True) # Field name made lowercase.
    minmatarstationtypeid = models.IntegerField(db_column='minmatarStationTypeID', blank=True, null=True) # Field name made lowercase.
    amarrstationtypeid = models.IntegerField(db_column='amarrStationTypeID', blank=True, null=True) # Field name made lowercase.
    gallentestationtypeid = models.IntegerField(db_column='gallenteStationTypeID', blank=True, null=True) # Field name made lowercase.
    jovestationtypeid = models.IntegerField(db_column='joveStationTypeID', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'staOperations'

class Staservices(models.Model):
    serviceid = models.IntegerField(db_column='serviceID', primary_key=True) # Field name made lowercase.
    servicename = models.CharField(db_column='serviceName', max_length=200, blank=True) # Field name made lowercase.
    description = models.CharField(max_length=2000, blank=True)
    class Meta:
        managed = False
        db_table = 'staServices'

class Stastationtypes(models.Model):
    stationtypeid = models.IntegerField(db_column='stationTypeID', primary_key=True) # Field name made lowercase.
    dockentryx = models.TextField(db_column='dockEntryX', blank=True) # Field name made lowercase. This field type is a guess.
    dockentryy = models.TextField(db_column='dockEntryY', blank=True) # Field name made lowercase. This field type is a guess.
    dockentryz = models.TextField(db_column='dockEntryZ', blank=True) # Field name made lowercase. This field type is a guess.
    dockorientationx = models.TextField(db_column='dockOrientationX', blank=True) # Field name made lowercase. This field type is a guess.
    dockorientationy = models.TextField(db_column='dockOrientationY', blank=True) # Field name made lowercase. This field type is a guess.
    dockorientationz = models.TextField(db_column='dockOrientationZ', blank=True) # Field name made lowercase. This field type is a guess.
    operationid = models.IntegerField(db_column='operationID', blank=True, null=True) # Field name made lowercase.
    officeslots = models.IntegerField(db_column='officeSlots', blank=True, null=True) # Field name made lowercase.
    reprocessingefficiency = models.TextField(db_column='reprocessingEfficiency', blank=True) # Field name made lowercase. This field type is a guess.
    conquerable = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'staStationTypes'

class Stastations(models.Model):
    stationid = models.IntegerField(db_column='stationID', primary_key=True) # Field name made lowercase.
    security = models.IntegerField(blank=True, null=True)
    dockingcostpervolume = models.TextField(db_column='dockingCostPerVolume', blank=True) # Field name made lowercase. This field type is a guess.
    maxshipvolumedockable = models.TextField(db_column='maxShipVolumeDockable', blank=True) # Field name made lowercase. This field type is a guess.
    officerentalcost = models.IntegerField(db_column='officeRentalCost', blank=True, null=True) # Field name made lowercase.
    operationid = models.IntegerField(db_column='operationID', blank=True, null=True) # Field name made lowercase.
    stationtypeid = models.IntegerField(db_column='stationTypeID', blank=True, null=True) # Field name made lowercase.
    corporationid = models.IntegerField(db_column='corporationID', blank=True, null=True) # Field name made lowercase.
    solarsystemid = models.IntegerField(db_column='solarSystemID', blank=True, null=True) # Field name made lowercase.
    constellationid = models.IntegerField(db_column='constellationID', blank=True, null=True) # Field name made lowercase.
    regionid = models.IntegerField(db_column='regionID', blank=True, null=True) # Field name made lowercase.
    stationname = models.CharField(db_column='stationName', max_length=200, blank=True) # Field name made lowercase.
    x = models.TextField(blank=True) # This field type is a guess.
    y = models.TextField(blank=True) # This field type is a guess.
    z = models.TextField(blank=True) # This field type is a guess.
    reprocessingefficiency = models.TextField(db_column='reprocessingEfficiency', blank=True) # Field name made lowercase. This field type is a guess.
    reprocessingstationstake = models.TextField(db_column='reprocessingStationsTake', blank=True) # Field name made lowercase. This field type is a guess.
    reprocessinghangarflag = models.IntegerField(db_column='reprocessingHangarFlag', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'staStations'

class Translationtables(models.Model):
    sourcetable = models.CharField(db_column='sourceTable', primary_key=True, max_length=400) # Field name made lowercase.
    destinationtable = models.CharField(db_column='destinationTable', max_length=400, blank=True) # Field name made lowercase.
    translatedkey = models.CharField(db_column='translatedKey', primary_key=True, max_length=400) # Field name made lowercase.
    tcgroupid = models.IntegerField(db_column='tcGroupID', blank=True, null=True) # Field name made lowercase.
    tcid = models.IntegerField(db_column='tcID', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'translationTables'

class Trntranslationcolumns(models.Model):
    tcgroupid = models.IntegerField(db_column='tcGroupID', blank=True, null=True) # Field name made lowercase.
    tcid = models.IntegerField(db_column='tcID', primary_key=True) # Field name made lowercase.
    tablename = models.CharField(db_column='tableName', max_length=512) # Field name made lowercase.
    columnname = models.CharField(db_column='columnName', max_length=256) # Field name made lowercase.
    masterid = models.CharField(db_column='masterID', max_length=256, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'trnTranslationColumns'

class Trntranslationlanguages(models.Model):
    numericlanguageid = models.IntegerField(db_column='numericLanguageID', primary_key=True) # Field name made lowercase.
    languageid = models.CharField(db_column='languageID', max_length=50, blank=True) # Field name made lowercase.
    languagename = models.CharField(db_column='languageName', max_length=400, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'trnTranslationLanguages'

class Trntranslations(models.Model):
    tcid = models.IntegerField(db_column='tcID', primary_key=True) # Field name made lowercase.
    keyid = models.IntegerField(db_column='keyID', primary_key=True) # Field name made lowercase.
    languageid = models.CharField(db_column='languageID', primary_key=True, max_length=50) # Field name made lowercase.
    text = models.TextField() # This field type is a guess.
    class Meta:
        managed = False
        db_table = 'trnTranslations'

class Warcombatzonesystems(models.Model):
    solarsystemid = models.IntegerField(db_column='solarSystemID', primary_key=True) # Field name made lowercase.
    combatzoneid = models.IntegerField(db_column='combatZoneID', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'warCombatZoneSystems'

class Warcombatzones(models.Model):
    combatzoneid = models.IntegerField(db_column='combatZoneID', primary_key=True) # Field name made lowercase.
    combatzonename = models.CharField(db_column='combatZoneName', max_length=200, blank=True) # Field name made lowercase.
    factionid = models.IntegerField(db_column='factionID', blank=True, null=True) # Field name made lowercase.
    centersystemid = models.IntegerField(db_column='centerSystemID', blank=True, null=True) # Field name made lowercase.
    description = models.CharField(max_length=1000, blank=True)
    class Meta:
        managed = False
        db_table = 'warCombatZones'