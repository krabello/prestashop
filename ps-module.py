import os, sys, urllib.request

moduleName = input('Module name: ')
moduleCategory = input('Module Category (others): ').replace(' ', '_')
if moduleCategory == '':
    moduleCategory = 'others'

moduleVersion = input('Module Version (1.0.0): ')
if moduleVersion == '':
    moduleVersion = '1.0.0'

moduleDescription = input('Module Description: ')

companyName = 'Catalog Solutions';
error = False

def createClassName():
    return companyName.replace(' ', '') + \
    moduleName.replace(' ', '').capitalize()

def technicalName():
    return moduleName.replace(' ', '')

def publicName():
    return moduleName.capitalize()

moduleFiles = [technicalName() + '.php', 'config.xml']
imgURLs = ['http://catalogsolutions.com/logo.png', 'http://catalogsolutions.com/logo.gif']

moduleDirectories = [
    technicalName(), technicalName() + '/views/templates/admin', technicalName() + '/views/templates/front', 
    technicalName() + '/views/templates/hook', technicalName() + '/views/css', technicalName() + '/views/js', 
    technicalName() + '/views/img', technicalName() + '/controllers', technicalName() + '/override', 
    technicalName() + '/themes/[theme_name]/modules', technicalName() + '/upgrade'
]

# Make a directory
def makeDirectory(directoryPath):
    try:
        if not os.path.exists(directoryPath):
            os.makedirs(directoryPath)
    except OSError:
        error = True
        raise error

# Creates file
def createFile(file):
    try:
        with open(file, "w") as f:
            f.truncate()
            f.write('<?php\n')
            f.write('\n')
            f.write('class ' + createClassName() + ' extends module\n')
            f.write('{\n')
            f.write('\t \n')
            f.write('\tpublic function __construct()\n')
            f.write('\t{\n')
            f.write('\t\t// Set the technical name. W/O this the module will\n')
            f.write('\t\t// not be able to be installed\n')
            f.write('\t\t$this->name = \'' + technicalName() + '\';\n')
            f.write('\t \n')
            f.write('\t\t// Set the Public name. This line is used to display\n')
            f.write('\t\t// the module name for the merchant in the modules\n')
            f.write('\t\t// list of the back office\n')
            f.write('\t\t$this->displayName = \'' + publicName() +'\';\n')
            f.write('\t\t \n')
            f.write('\t\t// Set the module category (optional) makes the module search easier\n')
            f.write('\t\t// administration\n')
            f.write('\t\t// advertising_marketing\n')
            f.write('\t\t// analytics_stats\n')
            f.write('\t\t// billing_invoicing\n')
            f.write('\t\t// Checkout\n')
            f.write('\t\t// content_management\n')
            f.write('\t\t// export\n')
            f.write('\t\t// emailing\n')
            f.write('\t\t// front_office_features\n')
            f.write('\t\t// i18n\n')
            f.write('\t\t// localization\n')
            f.write('\t\t// merchandizing\n')
            f.write('\t\t// migration_tools\n')
            f.write('\t\t// payments_gateways\n')
            f.write('\t\t// payment_security\n')
            f.write('\t\t// pricing_promotion\n')
            f.write('\t\t// quick_bulk_update\n')
            f.write('\t\t// search_filter\n')
            f.write('\t\t// seo\n')
            f.write('\t\t// shipping_logistics\n')
            f.write('\t\t// slideshows\n')
            f.write('\t\t// smart_shopping\n')
            f.write('\t\t// market_place\n')
            f.write('\t\t// social_networks\n')
            f.write('\t\t// others (default)\n')
            f.write('\t\t// mobile\n')
            f.write('\t\t$this->tab = \'' + moduleCategory + '\';\n')
            f.write('\t\t\n')
            f.write('\t\t// Set the module version\n')
            f.write('\t\t// display the module version in the module\'s \n')
            f.write('\t\t// list of the back office but also to check \n')
            f.write('\t\t// if updates are available\n')
            f.write('\t\t$this->version = \'' + moduleVersion + '\';\n')
            f.write('\t\t\n')
            f.write('\t\t// Set the author name: This line is used to \n')
            f.write('\t\t// display the author name for the merchant in \n')
            f.write('\t\t// the module\'s list of the back office. It can also \n')
            f.write('\t\t// be used to search for modules:\n')
            f.write('\t\t$this->author = \'Catalog Solutions\';\n')
            f.write('\t\t\n')
            f.write('\t\t// Set the module description\n')
            f.write('\t\t$this->description = \'' + moduleDescription + '\';\n')
            f.write('\t\t\n')
            f.write('\t\t// Call the parent contstructor. initializations\n')
            f.write('\t\t// are made in this function.\n')
            f.write('\t\tparent::__construct();\n')
            f.write('\t \n')
            f.write('\t}\n')
            f.write('}\n')
        f.close()
    except OSError:
        error = True
        raise error

def createXMLConfig(file):
    try:
        with open(file, "w") as f:
            f.truncate()
            f.write('<?xml version="1.0" encoding="UTF-8" ?>')
            f.write('\t<module>\n')
            f.write('\t\t<name>' + technicalName() + '</name>\n')
            f.write('\t\t<displayName><![CDATA[' + publicName() + ']]></displayName>\n')
            f.write('\t\t<version><![CDATA[' + moduleVersion + ']]></version>\n')
            f.write('\t\t<description><![CDATA[' + moduleDescription + ']]></description>\n')
            f.write('\t\t<author><![CDATA[' + companyName + ']]></author>\n')
            f.write('\t\t<tab><![CDATA[' + moduleCategory + ']]></tab>\n')
            f.write('\t\t<confirmUninstall>Are you sure you want to uninstall?</confirmUninstall>\n')
            f.write('\t\t<is_configurable>0</is_configurable>\n')
            f.write('\t\t<need_instance>0</need_instance>\n')
            f.write('\t\t<limited_countries></limited_countries>\n')
            f.write('\t</module>')
            f.close()
    except OSError:
        error = True
        raise error

# Create Directory Structure
for moduleDirectory in moduleDirectories:
    makeDirectory(moduleDirectory)

# Create files
for file in moduleFiles:
    print(file)
    if file == 'config.xml':
        createXMLConfig(technicalName() + '/' + file)
    else:
        createFile(technicalName() + '/' + file)

# Download logo images
for imgURL in imgURLs:
    file_name = imgURL.split('/')[-1].split('#')[0].split('?')[0]
    with urllib.request.urlopen(imgURL) as response, open(os.path.join(technicalName(), file_name), 'wb') as out_file:
        out_file.write(response.read())

if error:
    print('There was a error')
else:
    print(moduleName + " module created!")
