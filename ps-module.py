import os, sys, urllib.request, re
from string import whitespace

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

def ucwords(source):
    uc_source = ''
    for idx, a_char in enumerate(source):
        if a_char in whitespace or not a_char.isalpha():  # whitespace or not alpha is fine to add
            uc_source += a_char
        elif a_char.isalpha() and (not idx or source[idx - 1] in whitespace):  # we know we're alpha, and either the first character, or the one prev is whitespace
            uc_source += a_char.upper()
        else:  # whatever else we can be, let's add!
            uc_source += a_char
    return uc_source

def createClassName():
    return companyName.replace(' ', '') + \
    moduleName.replace(' ', '').capitalize()

def rootDirName():
    return companyName.replace(' ', '') + \
    ucwords(moduleName).replace(' ', '')

def technicalName():
    return moduleName.replace(' ', '')

def publicName():
    return moduleName.capitalize()

moduleFiles = [technicalName() + '.php', 'config.xml']
imgURLs = ['http://catalogsolutions.com/logo.png', 'http://catalogsolutions.com/logo.gif']

moduleDirectories = [
    rootDirName(), rootDirName() + '/views/templates/admin', rootDirName() + '/views/templates/front', 
    rootDirName() + '/views/templates/hook', rootDirName() + '/views/css', rootDirName() + '/views/js', 
    rootDirName() + '/views/img', rootDirName() + '/controllers', rootDirName() + '/override', 
    rootDirName() + '/themes/[theme_name]/modules', rootDirName() + '/upgrade'
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
            f.write('     \n')
            f.write('    public function __construct()\n')
            f.write('    {\n')
            f.write('        // Set the technical name. W/O this the module will\n')
            f.write('        // not be able to be installed\n')
            f.write('        $this->name = \'' + technicalName() + '\';\n')
            f.write('     \n')
            f.write('        // Set the Public name. This line is used to display\n')
            f.write('        // the module name for the merchant in the modules\n')
            f.write('        // list of the back office\n')
            f.write('        $this->displayName = \'' + publicName() +'\';\n')
            f.write('         \n')
            f.write('        // Set the module category (optional) makes the module search easier\n')
            f.write('        // administration\n')
            f.write('        // advertising_marketing\n')
            f.write('        // analytics_stats\n')
            f.write('        // billing_invoicing\n')
            f.write('        // Checkout\n')
            f.write('        // content_management\n')
            f.write('        // export\n')
            f.write('        // emailing\n')
            f.write('        // front_office_features\n')
            f.write('        // i18n\n')
            f.write('        // localization\n')
            f.write('        // merchandizing\n')
            f.write('        // migration_tools\n')
            f.write('        // payments_gateways\n')
            f.write('        // payment_security\n')
            f.write('        // pricing_promotion\n')
            f.write('        // quick_bulk_update\n')
            f.write('        // search_filter\n')
            f.write('        // seo\n')
            f.write('        // shipping_logistics\n')
            f.write('        // slideshows\n')
            f.write('        // smart_shopping\n')
            f.write('        // market_place\n')
            f.write('        // social_networks\n')
            f.write('        // others (default)\n')
            f.write('        // mobile\n')
            f.write('        $this->tab = \'' + moduleCategory + '\';\n')
            f.write('        \n')
            f.write('        // Set the module version\n')
            f.write('        // display the module version in the module\'s \n')
            f.write('        // list of the back office but also to check \n')
            f.write('        // if updates are available\n')
            f.write('        $this->version = \'' + moduleVersion + '\';\n')
            f.write('        \n')
            f.write('        // Set the author name: This line is used to \n')
            f.write('        // display the author name for the merchant in \n')
            f.write('        // the module\'s list of the back office. It can also \n')
            f.write('        // be used to search for modules:\n')
            f.write('        $this->author = \'Catalog Solutions\';\n')
            f.write('        \n')
            f.write('        // Set the module description\n')
            f.write('        $this->description = \'' + moduleDescription + '\';\n')
            f.write('        \n')
            f.write('        // Call the parent contstructor. initializations\n')
            f.write('        // are made in this function.\n')
            f.write('        parent::__construct();\n')
            f.write('     \n')
            f.write('    }\n')
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
            f.write('    <module>\n')
            f.write('        <name>' + technicalName() + '</name>\n')
            f.write('        <displayName><![CDATA[' + publicName() + ']]></displayName>\n')
            f.write('        <version><![CDATA[' + moduleVersion + ']]></version>\n')
            f.write('        <description><![CDATA[' + moduleDescription + ']]></description>\n')
            f.write('        <author><![CDATA[' + companyName + ']]></author>\n')
            f.write('        <tab><![CDATA[' + moduleCategory + ']]></tab>\n')
            f.write('        <confirmUninstall>Are you sure you want to uninstall?</confirmUninstall>\n')
            f.write('        <is_configurable>0</is_configurable>\n')
            f.write('        <need_instance>0</need_instance>\n')
            f.write('        <limited_countries></limited_countries>\n')
            f.write('    </module>')
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
        createXMLConfig(rootDirName() + '/' + file)
    else:
        createFile(rootDirName() + '/' + file)

# Download logo images
for imgURL in imgURLs:
    file_name = imgURL.split('/')[-1].split('#')[0].split('?')[0]
    with urllib.request.urlopen(imgURL) as response, open(os.path.join(rootDirName(), file_name), 'wb') as out_file:
        out_file.write(response.read())

if error:
    print('There was a error')
else:
    print(moduleName + " module created!")
