# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 07:48:14 2015

@author: Justin
"""
from benchlingapi import BenchlingAPI, BenchlingAPIException, \
    AquariumLoginError, BenchlingLoginError, BenchlingPortal
import coral as cor

from nose.tools import assert_equal, assert_true, assert_raises

def testBenchlingAPIConstruction():
    bench_api_key = 'sk_g7fo2vxkNUYNPkShOFIOmtY9ejIGE'
    aq_api_key = 'GwZdTb4jr8YL3wwmVi1QYfG6jeLzUYxkLSZ7BAIKnOc'
    aq_user = 'vrana'
    aq_url = 'http://54.68.9.194:81/api'
    credentials = [bench_api, aq_url, aq_user, aq_api_key]
    portal = BenchlingPortal(*credentials)
    print "Construction Test Passed"
    
    credentials = [bench_api+"G", aq_url, aq_user, aq_api_key]
    assert_raises(BenchlingLoginError, BenchlingPortal, *credentials)
    print "Benchlingloginerror test passed"
    
    credentials = [bench_api, aq_url+"G", aq_user, aq_api_key]
    assert_raises(AquariumLoginError, BenchlingPortal, *credentials)
    print "AqLoginError test 1 passed"
    
    credentials = [bench_api, aq_url, aq_user+"G", aq_api_key]
    assert_raises(AquariumLoginError, BenchlingPortal, *credentials)
    print "AqLoginError test 2 passed"
    
    credentials = [bench_api, aq_url, aq_user, aq_api_key+"G"]
    assert_raises(AquariumLoginError, BenchlingPortal, *credentials)
    print "AqLoginError test 3 passed"


def testBenchlingAquariumPortal():
    bench_api = 'sk_g7fo2vxkNUYNPkShOFIOmtY9ejIGE'
    portal = BenchlingPortal(bench_api, 'GwZdTb4jr8YL3wwmVi1QYfG6jeLzUYxkLSZ7BAIKnOc', 'vrana', 'http://54.68.9.194:81/api')
    #test on plasmid
    c = portal.getSequenceFromAquarium(11231)
    assert(type(c) == cor.DNA)
    
    #test on fragment
    c = portal.getSequenceFromAquarium(11229)
    assert(type(c) == cor.DNA)
    
    #test on yeast strain
    assert_raises(BenchlingAPIException, portal.getSequenceFromAquarium, 11638)
    
    #test on plasmid with no sharelink
    assert_raises(BenchlingAPIException, portal.getSequenceFromAquarium, 11825)

    #test on plasmid with no sharelink
    assert_raises(BenchlingAPIException, portal.getSequenceFromAquarium, 9883)

    #test on misformatted sharelink plasmid
    assert_raises(BenchlingAPIException, portal.getSequenceFromAquarium, 11691)

def testGibsonAssembler():
    bench_api_key = 'sk_g7fo2vxkNUYNPkShOFIOmtY9ejIGE'
    aq_api_key = 'GwZdTb4jr8YL3wwmVi1QYfG6jeLzUYxkLSZ7BAIKnOc'
    aq_user = 'vrana'
    aq_url = 'http://54.68.9.194:81/api'
    credentials = [bench_api_key, aq_url, aq_user, aq_api_key]
    portal = BenchlingPortal(*credentials)
    seq = portal.getAqFragmentSequence(11229)
    print seq
    
testGibsonAssembler()
#bench_api_key = 'sk_g7fo2vxkNUYNPkShOFIOmtY9ejIGE'
#aq_api_key = 'GwZdTb4jr8YL3wwmVi1QYfG6jeLzUYxkLSZ7BAIKnOc'
#aq_user = 'vrana'
#aq_url = 'http://54.68.9.194:81/api'
#credentials = [bench_api, aq_url, aq_user, aq_api_key]
#portal = BenchlingPortal(*credentials)
#print portal.getSequenceFromShareLink('https://benchling.com/s/k5Y05YM2/edit')