<?php

declare(strict_types=1);

namespace PlanB\Backend\Infrastructure\Repository\BoxType;

use Avoris\Util\DataType\DataType;
use Avoris\Util\Exception\InvalidMethod;
use Avoris\Util\Moment\MomentFormat;
use Avoris\Util\Arr;
use Override;
use PlanB\Backend\Converter\BoxType\PrimitiveToBoxTypeConverter;
use PlanB\Backend\Domain\BoxType\BoxType;
use PlanB\Backend\Domain\BoxType\BoxTypeRepository;
use PlanB\Backend\Infrastructure\PDO\Model\PDOParam;
use PlanB\Backend\Infrastructure\PDO\PDOInterface;
use PlanB\Backend\Infrastructure\Repository\PDORepository;

final readonly class PDOBoxTypeRepository extends PDORepository implements BoxTypeRepository
{
    private const DATE_FORMAT = MomentFormat::ATOM_NO_TZ->value;
    public function __construct(
        private PrimitiveToBoxTypeConverter $toBoxType,
        PDOInterface $client
    ) {
        parent::__construct($client);
    }


    #[Override]    
    public function find(int $id): ?BoxType
    {
        
                $query = <<<NATIVE_SQL
                    SELECT
                        bt.id AS boxTypeId,
                        bt.package_data_name AS name,
                        bt.package_data_description AS description,
                        bt.package_data_short_description AS shortDescription,
                        bt.package_data_pvp AS pvp,
                        bt.package_data_ean_code AS eanCode,
                        bt.package_data_external_code AS externalCode,
                        bt.package_data_pax AS pax,
                        bt.web_data_permalink AS webDataPermalink,
                        bt.web_data_virtual AS webDataVirtual,
                        bt.web_data_nights AS webDataNights,
                        bt.web_data_residences AS webData_residences,
                        bt.audit_trial_user_id AS auditTrialUserId,
                        bt.audit_trial_created_at AS auditTrialCreatedAt,
                        bt.audit_trial_updated_at AS auditTrialUpdatedAt,
                        bt.audit_trial_deleted AS auditTrialDeleted,
                        bt.audit_trial_deleted_at AS auditTrialDeletedAt,
                        bt.audit_trial_active AS auditTrialActive,                        
                    FROM box_types bt
                    WHERE bt.id AS :boxTypeId,
        NATIVE_SQL;

        $boxTypes= $this->execute($query, [
            new PDOParam(':boxId', DataType::INT, $id), 
        ], $this->toBoxType); 
        
        if(empty($boxTypes)){
            return null;
        }       
 
        return Arr::first($boxTypes);
        
    }

    #[Override]
    public function search(): array
    {
        $query = <<<NATIVE_SQL
                    SELECT
                        bt.id AS box_type_id,
                        bt.package_data_name AS name,
                        bt.package_data_description AS description,
                        bt.package_data_short_description AS shortDescription,
                        bt.package_data_pvp AS pvp,
                        bt.package_data_ean_code AS eanCcode,
                        bt.package_data_external_code AS externalCode,
                        bt.package_data_pax AS pax,
                        bt.web_data_permalink AS webDataPermalink,
                        bt.web_data_virtual AS webDataVirtual,
                        bt.web_data_nights AS webDataNights,
                        bt.web_data_residences AS webDataResidences,
                        bt.audit_trial_user_id AS auditTrialUserId,
                        bt.audit_trial_created_at AS auditTrialCreatedAt,
                        bt.audit_trial_updated_at AS auditTrialUpdatedAt,
                        bt.audit_trial_deleted AS auditTrial_deleted,
                        bt.audit_trial_deleted_at AS auditTrialDeletedAt,
                        bt.audit_trial_active AS auditTrialActive,
                        bti.url as imageUrl
                    FROM box_types bt
                    LEFT JOIN box_types_images bti ON (bti.box_type_id = bt.id AND bti.preview = true)
        NATIVE_SQL;
 
        return $this->execute($query, [], $this->toBoxType);
    }

    #[Override]
    public function insert(BoxType $boxType): BoxType
    {
       
        $query = <<<NATIVE_SQL
        INSERT INTO box_types (
            package_data_name,package_data_description,package_data_short_description,package_data_pvp,
            package_data_ean_code,package_data_external_code,package_data_pax,web_data_permalink,
            web_data_virtual,web_data_nights,web_data_residences,audit_trial_user_id,audit_trial_created_at,
            audit_trial_updated_at,audit_trial_deleted,audit_trial_deleted_at,audit_trial_active,
        )
        VALUES
        (
            :packageDataName,:packageData_description,:packageData_short_description,:packageDataPvp,
            :packageDataEanCode,:packageDataExternalCode,:packageData_pax,:web_data_permalink,
            :web_data_virtual,:web_data_nights,:web_data_residences,:audit_trial_user_id,
            :audit_trial_created_at,:audit_trial_updated_at,:audit_trial_deleted,:audit_trial_deleted_at,
            :audit_trial_active,
        )
        NATIVE_SQL;


        $this->execute($query,
            [
                
                new PDOParam(':packageData_name',DataType::STRING,$boxType->packageData()->name()),
                new PDOParam(':packageData_description',DataType::STRING,$boxType->packageData()->description()),
                new PDOParam(':packageData_short_description',DataType::STRING,$boxType->packageData()->shortDescription()),                
                new PDOParam(':packageDataPvp',DataType::STRING,$boxType->packageData()->pvp()),
                new PDOParam(':packageDataEanCode',DataType::STRING,$boxType->packageData()->eanCode()),
                new PDOParam(':packageDataExternalCode',DataType::STRING,$boxType->packageData()->externalCode()),
                new PDOParam(':packageData_pax',DataType::STRING,$boxType->packageData()->pax()),

                new PDOParam(':webDataPermalink',DataType::STRING,$boxType->webData()->permalink()),
                new PDOParam(':webDataVirtual',DataType::STRING,$boxType->webData()->virtual()),
                new PDOParam(':webDataNights',DataType::STRING,$boxType->webData()->nights()),
                new PDOParam(':webDataResidences',DataType::STRING,$boxType->webData()->residences()),

                new PDOParam(':auditTrialUserId',DataType::INT,$boxType->auditTrial()->userId()),
                new PDOParam(':auditTrialCreatedAt',DataType::DATE_TIME,$boxType->auditTrial()->createdAt()->format(self::DATE_FORMAT)),
                new PDOParam(':auditTrialUpdatedAt',DataType::DATE_TIME,$boxType->auditTrial()->updatedAt()->format(self::DATE_FORMAT)),
                new PDOParam(':auditTrialDeleted',DataType::BOOL,$boxType->auditTrial()->deleted()),
                new PDOParam(':auditTrialDeletedAt',DataType::DATE_TIME,$boxType->auditTrial()->deletedAt()->format(self::DATE_FORMAT)),
                new PDOParam(':auditTrialActive',DataType::BOOL,$boxType->auditTrial()->active()),
            ]
            );
            return new BoxType(
                (int) $this->getLastInsertedId(),
                $boxType->packageData(),
                $boxType->webData(),
                $boxType->auditTrial(),
                $boxType->imageUrl()
            );
    }

    #[Override]
    public function save(BoxType $boxType): void
    {
         $query = <<<NATIVE_SQL
         UPDATE box_types
         SET
            package_data_name=:name,
            package_data_description=:description,
            package_data_short_description=:shortDescription,
            package_data_pvp=:pvp,
            package_data_ean_code=:eanCode,
            package_data_external_code=:externalCode,
            package_data_pax=:pax,
            web_data_permalink=:webDataPermalink,
            web_data_virtual=:webDataVirtual,
            web_data_nights=:webDataNights,
            web_data_residences=:webDataResidences,
            audit_trial_user_id=:auditTrialUser_id,
            audit_trial_created_at=:auditTrialCreated_at,
            audit_trial_updated_at=:auditTrialUpdated_at,
            audit_trial_deleted=:auditTrialDeleted,
            audit_trial_deleted_at=:auditTrialDeleted_at,
            audit_trial_active=:auditTrialActive
        WHERE
            id = :boxTypeId 
        NATIVE_SQL;


        $this->execute($query,
            [
                // ---> arreglar los espacios
                new PDOParam(':name',DataType::STRING,$boxType->packageData()->name()),
                new PDOParam(':description',DataType::STRING,$boxType->packageData()->description()),
                new PDOParam(':shortDescription',DataType::STRING,$boxType->packageData()->shortDescription()),
                
                new PDOParam(':pvp',DataType::STRING,$boxType->packageData()->pvp()),
                new PDOParam(':eanCode',DataType::STRING,$boxType->packageData()->eanCode()),
                new PDOParam(':externalCode',DataType::STRING,$boxType->packageData()->externalCode()),
                new PDOParam(':pax',DataType::STRING,$boxType->packageData()->pax()),

                new PDOParam(':webDataPermalink',DataType::STRING,$boxType->webData()->permalink()),
                new PDOParam(':webDataVirtual',DataType::STRING,$boxType->webData()->virtual()),
                new PDOParam(':webDataNights',DataType::STRING,$boxType->webData()->nights()),
                new PDOParam(':webDataResidences',DataType::STRING,$boxType->webData()->residences()),

                new PDOParam(':auditTrialUserId',DataType::INT,$boxType->auditTrial()->userId()),
                new PDOParam(':auditTrialCreatedAt',DataType::DATE_TIME,$boxType->auditTrial()->createdAt()->format(self::DATE_FORMAT)),
                new PDOParam(':auditTrialUpdatedAt',DataType::DATE_TIME,$boxType->auditTrial()->updatedAt()->format(self::DATE_FORMAT)),
                new PDOParam(':auditTrialDeleted',DataType::BOOL,$boxType->auditTrial()->deleted()),
                new PDOParam(':auditTrialDeletedAt',DataType::DATE_TIME,$boxType->auditTrial()->deletedAt()->format(self::DATE_FORMAT)),
                new PDOParam(':auditTrialActive',DataType::BOOL,$boxType->auditTrial()->active()),
                new PDOParam(':boxTypeId',DataType::BOOL,$boxType->id()),
            ]
            );

    }


}
